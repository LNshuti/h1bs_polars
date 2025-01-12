#### H-1B Visa Lottery Dashboard PRD

Develop an interactive, data-rich dashboard using Vervel to analyze and visualize the H-1B visa lottery system. This dashboard will allow users to explore key metrics such as employer participation, salaries, job titles, and country of origin through detailed filters and visualizations. The goal is to enable users to uncover trends, disparities, and systemic issues intuitively.

#### Implementation Details
##### Core Filters
##### By Year:
###### Column(s): fiscal_year, rec_date.
##### Behavior: Users select a specific year or range of years.
##### Use Case: Identify trends over time, such as changes in approvals or registrations.
##### By Employer:
#### Column(s): employer_name, i129_employer_name.
##### Behavior: Search or multi-select specific employers (e.g., Wipro, Amazon).
##### Use Case: Compare approval rates and average salaries between employers.
##### By Job Title:
##### Column(s): job_title.
##### Behavior: Filter by title or keyword (e.g., “Software Engineer”).
##### Use Case: Evaluate common roles and associated salaries.
##### By Country of Origin:
##### Column(s): country_of_birth, country_of_nationality.
##### Behavior: Interactive selection via a world map or dropdown.
##### Use Case: Drill into disparities in registrations or approvals by applicant nationality.
##### By Salary Range:
##### Column(s): wage_amt, wage_unit.
##### Behavior: Set a numeric range (e.g., $50,000–$150,000).
##### Use Case: Compare salary trends across job titles or employers.
##### By Lottery Participation:
##### Column(s): ben_multi_reg_ind.
##### Behavior: Binary filter to show single vs. multiple registrations.
##### Use Case: Identify potential instances of lottery "gaming."
##### By Worksite:
##### Column(s): worksite_city, worksite_state.
##### Behavior: Search by city/state or select from a map.
##### Use Case: Examine geographic distribution of visa allocations.
##### Approval Status:
##### Column(s): status_type, first_decision.
##### Behavior: Filter by approval, denial, or pending status.
##### Use Case: Assess processing outcomes.

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


