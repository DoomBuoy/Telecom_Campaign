                                                                                    |
# Telecom_Campaign

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

A telecommunication company recently launched a marketing campaign to promote the adoption of their new subscription plan among customers. This Project provides assistance in gaining a comprehensive understanding of their customers and identifying the customer segments that display the highest responsiveness to marketing campaigns.
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

