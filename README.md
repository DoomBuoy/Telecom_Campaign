                                                                                    |
# Telecom_Campaign

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A telecommunication company recently launched a marketing campaign to promote the adoption of their new subscription plan among customers. This Project provides assistance in gaining a comprehensive understanding of their customers and identifying the customer segments that display the highest responsiveness to marketing campaigns.


This EDA provides a thorough understanding of the dataset's structure, distributions, relationships, and potential challenges for further analysis or modeling.

**Data science and visualization techniques** are central to this project, enabling the extraction of actionable insights from complex customer data. Through a combination of statistical analysis and rich visualizations (such as histograms, boxplots, pie charts, and heatmaps), the project uncovers patterns, trends, and key drivers of customer behavior. These visual tools not only make the data more accessible but also support informed decision-making for targeted marketing strategies in the telecom sector.


This project's jupyter notebook performs a comprehensive Exploratory Data Analysis (EDA) on the Telecom Campaign dataset. The key steps and analyses include:

- Data Import & Cleaning: The raw CSV data is cleaned using string manipulation to correct formatting issues, remove extraneous quotes, and standardize column names and values.
- Initial Exploration: The dataset's structure is examined, including data types, summary statistics, and checks for missing or duplicate values (with duplicates removed).
- Categorical Feature Analysis: Categorical variables are described and visualized using pie and bar charts. The distribution of categories and class imbalance in the target variable are highlighted.
- Chi-Squared Test: The association between categorical features and the target variable is assessed using the chi-squared test, identifying the most predictive categorical features.
- Analysis of 'Unknown' Values: The frequency and percentage of 'unknown' values in categorical features are calculated and visualized to assess data quality.
- Numerical Feature Analysis: Numerical variables are explored with descriptive statistics, histograms, and boxplots. Outliers are detected and quantified using the IQR method.
- Correlation Analysis: Correlation matrices and heatmaps are generated to examine relationships between numerical features and the target. Strongly correlated features are visualized with scatter plots.
- Summary: The notebook concludes with a summary of findings, highlighting key patterns, data quality issues, and features most relevant for modeling.

This EDA provides a thorough understanding of the dataset's structure, distributions, relationships, and potential challenges for further analysis or modeling.
# Data Card

| Variable         | Description                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| age              | Age                                                                                                                                |
| job              | Type of job                                                                                                                        |
| marital          | Marital status                                                                                                                     |
| education        | Level of education                                                                                                                 |
| default          | Has credit in default                                                                                                              |
| balance          | Average yearly balance                                                                                                             |
| housing          | Has a housing loan                                                                                                                 |
| loan             | Has a personal loan                                                                                                                |
| contact          | Contact communication type                                                                                                         |
| day              | Day of contact                                                                                                                     |
| month            | Month of contact                                                                                                                   |
| duration         | Last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. |
| campaign         | Number of contacts performed during this campaign and for this client                                                              |
| pdays            | Number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted) |
| previous         | Number of contacts performed before this campaign and for this client                                                              |
| poutcome         | Outcome of the previous marketing campaign                                                                                        |
| emp.var.rate     | Employment variation rate - quarterly indicator (numeric)                                                                          |
| cons.price.idx   | Consumer price index - monthly indicator (numeric)                                                                                 |
| cons.conf.idx    | Consumer confidence index - monthly indicator (numeric)                                                                            |
| euribor3m        | Euribor 3 month rate - daily indicator (numeric)                                                                                   |
| nr.employed      | Number employed - quarterly indicator (numeric)                                                                                    |
| y                | Did the client subscribe to a Telecom plan?    
## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
│
├── docs               <- Include docs for report.
│
│
│
├── notebooks          <- Jupyter notebooks. 
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         telecom_campaign and configuration for tools like black
│
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└──── setup.cfg          <- Configuration file for flake8

```

--------

