import pandas as pd
import gradio as gr
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    
    # Handle missing values explicitly
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    datetime_cols = data.select_dtypes(include=['datetime64[ns]']).columns
    
    data[numeric_cols] = data[numeric_cols].fillna(-1)  # Placeholder for numeric columns
    data[datetime_cols] = data[datetime_cols].fillna(pd.Timestamp("1970-01-01"))  # Placeholder for datetime
    data.fillna("Unknown", inplace=True)  # Remaining columns
    
    return data

# Load dataset
DATA_PATH = "data/TRK_13139_FY2021_2023.csv"
data = load_and_clean_data(DATA_PATH)

# Function to filter the dataset
def filter_data(fiscal_year, employer, job_title, country_of_birth, country_of_nationality, min_salary, max_salary, worksite_city, worksite_state):
    filtered = data.copy()
    
    if fiscal_year != "All":
        filtered = filtered[filtered['fiscal_year'] == int(fiscal_year)]
    if employer != "All":
        filtered = filtered[filtered['employer_name'] == employer]
    if job_title != "All":
        filtered = filtered[filtered['job_title'] == job_title]
    if country_of_birth != "All":
        filtered = filtered[filtered['country_of_birth'] == country_of_birth]
    if country_of_nationality != "All":
        filtered = filtered[filtered['country_of_nationality'] == country_of_nationality]
    if min_salary:
        filtered = filtered[filtered['wage_amt'] >= float(min_salary)]
    if max_salary:
        filtered = filtered[filtered['wage_amt'] <= float(max_salary)]
    if worksite_city != "All":
        filtered = filtered[filtered['worksite_city'] == worksite_city]
    if worksite_state != "All":
        filtered = filtered[filtered['worksite_state'] == worksite_state]
        
    return filtered

# Function to generate insights and visualizations
def generate_visuals(filtered_data):
    # Gender Distribution Bar Chart
    plt.figure(figsize=(12, 8))
    sns.countplot(data=filtered_data, x='gender', order=filtered_data['gender'].value_counts().index)
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    gender_chart = gr.Plot(plt.gcf())

    # Country of Birth Distribution
    plt.figure(figsize=(12, 8))
    filtered_data['country_of_birth'].value_counts().head(10).plot(kind='bar', color='skyblue')
    plt.title("Top 10 Countries of Birth")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.tight_layout()
    country_chart = gr.Plot(plt.gcf())
    
    # Salary by Gender Histogram
    plt.figure(figsize=(12, 8))
    sns.histplot(data=filtered_data, x='wage_amt', hue='gender', multiple="stack", kde=True)
    plt.title("Salary Distribution by Gender")
    plt.xlabel("Salary (USD)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    salary_gender_hist = gr.Plot(plt.gcf())

    return gender_chart, country_chart, salary_gender_hist

# Function to export filtered data to CSV
def export_to_csv(filtered_data):
    csv_file_path = "filtered_data.csv"
    filtered_data.to_csv(csv_file_path, index=False)
    return csv_file_path

# Gradio Interface
def app(fiscal_year, employer, job_title, country_of_birth, country_of_nationality, min_salary, max_salary, worksite_city, worksite_state):
    filtered = filter_data(fiscal_year, employer, job_title, country_of_birth, country_of_nationality, min_salary, max_salary, worksite_city, worksite_state)
    gender_chart, country_chart, salary_gender_hist = generate_visuals(filtered)
    return filtered, gender_chart, country_chart, salary_gender_hist

# Dropdown options
fiscal_years = ["All"] + sorted(data['fiscal_year'].dropna().unique().astype(str).tolist())
employers = ["All"] + sorted(data['employer_name'].dropna().unique().tolist())
job_titles = ["All"] + sorted(data['job_title'].dropna().unique().tolist())
countries_of_birth = ["All"] + sorted(data['country_of_birth'].dropna().unique().tolist())
countries_of_nationality = ["All"] + sorted(data['country_of_nationality'].dropna().unique().tolist())
worksite_cities = ["All"] + sorted(data['worksite_city'].dropna().unique().tolist())
worksite_states = ["All"] + sorted(data['worksite_state'].dropna().unique().tolist())

# Gradio components
with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("### Data Exploration Dashboard")

    with gr.Row():
        fiscal_year = gr.Dropdown(label="Fiscal Year", choices=fiscal_years)
        employer = gr.Dropdown(label="Employer", choices=employers)
        job_title = gr.Dropdown(label="Job Title", choices=job_titles)

    with gr.Row():
        country_of_birth = gr.Dropdown(label="Country of Birth", choices=countries_of_birth)
        country_of_nationality = gr.Dropdown(label="Country of Nationality", choices=countries_of_nationality)

    with gr.Row():
        min_salary = gr.Textbox(label="Min Salary (USD)")
        max_salary = gr.Textbox(label="Max Salary (USD)")

    with gr.Row():
        worksite_city = gr.Dropdown(label="Worksite City", choices=worksite_cities)
        worksite_state = gr.Dropdown(label="Worksite State", choices=worksite_states)

    with gr.Row():
        apply_filters = gr.Button("Apply Filters")
    
    # Output components
    output_table = gr.Dataframe(label="Filtered Data")
    gender_chart = gr.Plot()
    country_chart = gr.Plot()
    salary_gender_hist = gr.Plot()

    apply_filters.click(
        app,
        inputs=[fiscal_year, employer, job_title, country_of_birth, country_of_nationality, min_salary, max_salary, worksite_city, worksite_state],
        outputs=[output_table, gender_chart, country_chart, salary_gender_hist]
    )

    # Export button
    export_button = gr.Button("Export Filtered Data as CSV", elem_id="export-button", elem_classes="large-button")
    
    # Export functionality
    export_button.click(
        export_to_csv,
        inputs=output_table,
        outputs=gr.File(label="Download CSV")
    )

# Custom CSS for the button
demo.css = """
.large-button {
    background-color: #4CAF50; /* Green */
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border: none;
    border-radius: 4px;
}
"""

demo.launch()