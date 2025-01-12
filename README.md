#### H-1B Visa Lottery Dashboard 

Interactive, data-rich dashboard to analyze and visualize the United States H-1B visa lottery system. Explore key metrics such as employer participation, salaries, job titles, and country of origin through detailed filters and visualizations. 

#### Core Filters
##### Year:
##### fiscal_year, rec_date.
##### Select a specific year or range of years.
##### Identify changes in approvals or registrations.
##### By employer_name, i129_employer_name.
##### Behavior: Search or multi-select specific employers (e.g., Wipro, Amazon).
##### Use Case: Compare approval rates and average salaries between employers.
##### By Job Title:
##### Column(s): job_title.
##### Behavior: Filter by title or keyword (e.g., “Software Engineer”).
##### Use Case: Evaluate common roles and associated salaries.
##### By Country of birth, country_of_nationality.
##### Interactive selection via a world map or dropdown to Drill into disparities in registrations or approvals by applicant nationality.
##### By Salary Range: wage_amt, wage_unit. Compare salary trends across job titles or employers.
##### By Lottery Participation: ben_multi_reg_ind.
##### Binary filter to show single vs. multiple registrations.
##### Identify potential instances of lottery "gaming."
##### By Worksite: worksite_city, worksite_state.
##### Behavior: Search by city/state or select from a map.
##### Use Case: Examine geographic distribution of visa allocations by approval, denial, or pending status.

#### User Flow
#### Landing Page
#### Elements: Key summary visualizations (e.g., total approvals, top employers).
##### Actions: Click any summary to dive deeper.
##### Filters Available: Year, Employer, Job Title.
#### Country of Origin Analysis
#### View: Interactive world map showing registrations and approvals by country.
#### User Actions:
#### Click a country to view granular data (e.g., top employers, job titles).
Apply additional filters (e.g., fiscal year, job title).
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
User Actions:
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


