# * Deploy preprocessed H1B historical data converted from zipped csv files to parquet. 

## The file saved under ./load_datasette.py loads three files assiciated with the 2021-2023
## H1B lotteries obtained by Bloomberg through a FOIA request available on Github 
## The script removes fields missing > 70 percent of the observations, uses simple 
## Imputation to replace numeric fields from the median, and categorical fields with the mode. 

# The preprocessed data is saved under ./data/TRK_13139_FY2021_2023.parquet 

# The data is then written to a local database ./data/datasette.db which this 
# Script deploys to modal(modal.com) following the example in their github repo
# https://github.com/modal-labs/modal-examples/blob/main/10_integrations/covid_datasette.py

import asyncio 
import pathlib 
import shutil 
import tempfile 
from datetime import datetime 

import modal 

# Configure application
APP_NAME = "h1b-data-explorer"
DB_FILENAME = "datasette.db"
VOLUME_DIR = "/cache-vol"
DB_PATH = pathlib.Path(VOLUME_DIR) / DB_FILENAME
LOCAL_DB_PATH = "./data/datasette.db"

# Initialize Modal app and resources
app = modal.App(APP_NAME)
volume = modal.Volume.from_name(f"{APP_NAME}-vol", create_if_missing=True)

# Configure the container image
datasette_image = (
    modal.Image.debian_slim()
    .pip_install(
        "datasette~=0.63.2",
        "sqlite-utils",
    )
)

@app.function(
    image=datasette_image,
    volumes={VOLUME_DIR: volume},
    timeout=900,
    retries=2,
)
def prep_db():
    """
    Copy the existing database to the Modal volume
    """
    import sqlite_utils
    
    print(f"Starting database preparation at {datetime.now()}")
    volume.reload()

    # Process data in a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = pathlib.Path(tmpdir)
        tmp_db_path = tmpdir_path / DB_FILENAME
        
        # Copy local database to temp directory
        print(f"Copying database from {LOCAL_DB_PATH}")
        shutil.copyfile(LOCAL_DB_PATH, tmp_db_path)
        
        # Verify database and create indices
        db = sqlite_utils.Database(tmp_db_path)
        
        try:
            # Create indices for better query performance
            print("Creating indices...")
            db["trk_data"].create_index(["employer_name"], if_not_exists=True)
            db["trk_data"].create_index(["status_type"], if_not_exists=True)
            db["trk_data"].create_index(["rec_date"], if_not_exists=True)
            
        finally:
            db.close()
        
        # Copy to volume
        print(f"Copying database to volume path: {DB_PATH}")
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(tmp_db_path, DB_PATH)

    print("Syncing database with volume...")
    volume.commit()
    print("Database update completed successfully.")

@app.function(
    schedule=modal.Period(hours=24),
    timeout=1000,
    retries=3
)
def refresh_db():
    """Scheduled task to refresh the database daily."""
    print(f"Starting scheduled refresh at {datetime.now()}")
    try:
        prep_db.remote()
        print("Database refresh completed successfully")
    except Exception as e:
        print(f"Error during database refresh: {str(e)}")
        raise

@app.function(
    image=datasette_image,
    volumes={VOLUME_DIR: volume},
    allow_concurrent_inputs=16,
)
@modal.asgi_app()
def ui():
    """Serve the Datasette web interface."""
    from datasette.app import Datasette
    
    ds = Datasette(
        files=[DB_PATH],
        settings={
            "sql_time_limit_ms": 10000,
            "default_page_size": 50,
            "max_returned_rows": 2000,
            "allow_download": True,
            "default_cache_ttl": 300,
        },
        metadata={
            "title": "H1B Visa Data Explorer",
            "description": "Historical H1B visa application data from 2021-2023",
            "source": "Bloomberg FOIA Request",
            "source_url": "https://github.com/bloomberg/",
            "databases": {
                DB_FILENAME: {
                    "tables": {
                        "trk_data": {
                            "sortable_columns": [
                                "employer_name",
                                "status_type",
                                "rec_date",
                                "wage_amt"
                            ],
                            "facets": [
                                "status_type",
                                "state",
                                "requested_class"
                            ]
                        },
                        "country_iso_codes": {
                            "sortable_columns": ["country_name", "iso3"]
                        }
                    }
                }
            }
        }
    )
    
    asyncio.run(ds.invoke_startup())
    return ds.app()

@app.local_entrypoint()
def run():
    print("Setting up H1B visa database...")
    prep_db.remote()

if __name__ == "__main__":
    run()


