<h2 align="center" style="margin-top:-10px">H-1B Visa Lottery Dashboard</h2> 

Interactive dashboard of the United States H-1B visa lottery system. Explore key metrics such as employer participation, salaries, job titles, and country of origin through detailed filters and visualizations. 

### **Core Filters.** 
1. Fiscal year
2. Employer name (e.g., Wipro, Amazon).
3. Job title: (e.g., “Software Engineer”).
4. Country of birth, country of nationality.
5. Salary Range: wage amt(e.g. $50,000), wage unit(e.g. year).
6. Worksite: worksite_city, worksite_state.

## Explore the Data live with Datasette(SQLITE) deployed on Modal 

- 🔸 ✶ [H1Bs Database](https://lnshuti--h1b-data-explorer-ui.modal.run)

# Demo 

![Datasette Demo](honebs_cleaned.gif)

### Example query

```json
SELECT 
    employer_name, 
    first_decision, 
    ben_sex, 
    ben_country_of_birth, 
    COUNT(1) AS city,
    SUM(COUNT(1)) OVER (PARTITION BY employer_name ORDER BY first_decision) AS cumulative_sum
FROM (
    SELECT 
        employer_name,
        first_decision,
        ben_sex,
        ben_country_of_birth
    FROM trk_data
) subquery
GROUP BY employer_name, first_decision, ben_sex, ben_country_of_birth
ORDER BY cumulative_sum desc, first_decision desc, employer_name;
```

### Add [result](https://lnshuti--h1b-data-explorer-ui.modal.run/datasette?sql=SELECT+%0D%0A++++employer_name%2C+%0D%0A++++first_decision%2C+%0D%0A++++ben_sex%2C+%0D%0A++++ben_country_of_birth%2C+%0D%0A++++COUNT%281%29+AS+city%2C%0D%0A++++SUM%28COUNT%281%29%29+OVER+%28PARTITION+BY+employer_name+ORDER+BY+first_decision%29+AS+cumulative_sum%0D%0AFROM+%28%0D%0A++++SELECT+%0D%0A++++++++employer_name%2C%0D%0A++++++++first_decision%2C%0D%0A++++++++ben_sex%2C%0D%0A++++++++ben_country_of_birth%0D%0A++++FROM+trk_data%0D%0A%29+subquery%0D%0AGROUP+BY+employer_name%2C+first_decision%2C+ben_sex%2C+ben_country_of_birth%0D%0AORDER+BY+cumulative_sum+desc%2C+first_decision+desc%2C+employer_name%3B)

### **Figure 1:** Salary of H1B recipients from Ukraine earning > $50,000

![image](https://github.com/user-attachments/assets/e5277697-77aa-4879-90de-df6ad1d63581)

### **Figure 2:** Salary of H1B recipients of all nationalities residing in Seatte, earning > $35,000

![image](https://github.com/user-attachments/assets/332c05a3-db8e-402e-b40f-098a4e5701dc)

### **Figure 3:** Software Engineer H1B recipients

![image](https://github.com/user-attachments/assets/34f1405f-8272-4be9-b0b2-c64d6dded56f)


### Visualizations:
- Time-series chart: Registrations vs. approvals by year.
- Treemap: Multiple vs. single registrations.

### Citations

1. US H-1B Visa Lottery and Petition Data FY 2021 - FY 2024. Data sourced from USCIS and obtained by Bloomberg.  https://github.com/BloombergGraphics/2024-h1b-immigration-data
