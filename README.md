#### H-1B Visa Lottery Dashboard 

Interactive, data-rich dashboard to analyze and visualize the United States H-1B visa lottery system. Explore key metrics such as employer participation, salaries, job titles, and country of origin through detailed filters and visualizations. 

#### Core Filters
##### Year:
##### fiscal_year
##### Identify changes in approvals or registrations.
##### By employer_name (e.g., Wipro, Amazon).
##### Use Case: Compare approval rates and average salaries between employers.
##### By Job Title: (e.g., “Software Engineer”).
##### By Country of birth, country_of_nationality.
##### By Salary Range: wage_amt, wage_unit. Compare salary trends across job titles or employers.
##### By Worksite: worksite_city, worksite_state.
##### Behavior: Search by city/state or select from a map.

#### User Flow
#### Landing Page
##### Filters Available: Year, Employer, Job Title.
#### Click a country to view granular data (e.g., top employers, job titles).
Visualizations:
Heat map (geographic distribution).
Drill-down bar charts (country-specific data).
Employer Insights
View: Bar chart of top employers by registrations/approvals.
User Actions:
Select an employer to view salary distributions or approval rates.
Add filters (e.g., year, job title).
Visualizations:
Bar chart: Registrations/approvals by employer.
Scatter plot: Approval rates vs. average salaries.
Network graph: Employer-applicant relationships.
Salary and Job Title Trends
View: Salary distributions for selected job titles and employers.
Filter by salary range or job title.
Highlight outliers (e.g., unusually low/high salaries).
Visualizations:
Box plot: Salary ranges across employers/job titles.
Word cloud: Most common job titles.
#### Lottery Disparities
#### View: Trend analysis of lottery participation and approval over time.
#### User Actions:
Filter by employer, country, or fiscal year.
Toggle between single and multiple registrations.
Visualizations:
Time-series chart: Registrations vs. approvals by year.
Treemap: Multiple vs. single registrations.

#### Visualization Types
Bar Charts: For employer rankings and registration counts.
Heat Maps: Geographical distribution of visa applicants.
Scatter Plots: Employer approval rates vs. average salaries.
#### Box Plots: Salary comparisons.
Word Clouds: Common job titles.
Treemaps: Visualizing lottery disparities.
Time-Series Charts: Trends over time.

#### Success Metrics
#### Engagement Metrics:
Average session time: Target 10+ minutes.
Filter usage: At least 5 filters applied per session.
Downloads: 500+ visualizations/datasets per quarter.
#### Performance Metrics:
Load time: <3 seconds for datasets up to 10M rows.
Dynamic filtering: Visualizations update instantly (<1 second).

#### Technical Considerations
Framework: Vervel for visualization and data handling.
Data Storage: Cloud-based backend optimized for large datasets.
Performance Enhancements:
Pre-compute aggregates for common filters.
Lazy loading for large visualizations.


