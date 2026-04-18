# Student Performance Statistical Analysis

This repository contains the first stage of a project for the course **Statistics and Queueing Theory**. The current stage focuses on the statistical analysis part of the project, using the UCI Student Performance dataset.

The queueing theory and event-driven simulation part will be added later as a separate stage.

## Project Scope

The statistical part of the project covers two main areas:

1. **Statistical hypothesis testing**
   - formulate research questions based on student characteristics and final grades,
   - compare groups using appropriate statistical tests,
   - interpret p-values, confidence intervals, and practical meaning of the results.

2. **Multiple regression analysis**
   - build a regression model for predicting the final grade,
   - evaluate model quality and explanatory power,
   - analyze residuals and check model assumptions.

## Dataset

The project uses the **Student Performance** dataset from the UCI Machine Learning Repository.

The dataset describes student achievement in secondary education in two Portuguese schools. It includes demographic, social, school-related, and academic variables collected from school reports and questionnaires.

Two subject-specific datasets are available:

- Mathematics course data,
- Portuguese language course data.

The main target variable is:

- `G3` - final grade, numeric value from 0 to 20.

The dataset also contains earlier grades:

- `G1` - first period grade,
- `G2` - second period grade.

Because `G1` and `G2` are strongly correlated with `G3`, the main regression model should be built without them. This makes the prediction task harder, but also more meaningful because the model relies on background, behavioral, and school-related factors instead of earlier grades that directly precede the final grade.

## Planned Statistical Questions

Possible hypothesis tests include:

- whether students with internet access at home achieve different final grades than students without internet access,
- whether students receiving extra educational support differ in final grade from students who do not receive such support,
- whether students with past class failures achieve lower final grades,
- whether study time is associated with final grade,
- whether school absences are related to academic performance.

The final set of tests will be selected after exploratory data analysis.

## Planned Regression Model

The main regression task is to explain or predict `G3`, the final grade.

Potential explanatory variables include:

- `studytime` - weekly study time,
- `failures` - number of past class failures,
- `absences` - number of school absences,
- `Medu` - mother's education level,
- `Fedu` - father's education level,
- `traveltime` - travel time from home to school,
- `schoolsup` - extra educational support,
- `internet` - internet access at home,
- `higher` - intention to pursue higher education,
- selected demographic and social variables.

The regression analysis should include:

- model estimation,
- coefficient interpretation,
- goodness-of-fit measures,
- statistical significance of predictors,
- residual diagnostics,
- detection of outliers or influential observations.

## Current Files

- `analysis.py` - initial Python script that fetches the dataset from UCI and displays basic information.
- `start_info.md` - cleaned dataset description and variable reference.
- `report.docx` - placeholder for the final report.

## Tools and Libraries

The current script uses:

- Python,
- `ucimlrepo`.

Planned analysis will likely require:

- `pandas`,
- `numpy`,
- `scipy`,
- `statsmodels`,
- `matplotlib`,
- `seaborn`.

## How to Run

Install the required package for loading the dataset:

```bash
pip install ucimlrepo
```

Run the current script:

```bash
python analysis.py
```

At this stage, the script only downloads the dataset and prints basic information about features and target variables.

## Project Status

Current status:

- dataset selected,
- statistical direction accepted,
- initial data loading script created,
- project documentation started.

Next steps:

- extend `analysis.py` with exploratory data analysis,
- select concrete hypotheses,
- implement statistical tests,
- build and evaluate a multiple regression model,
- prepare plots and interpretation for the report.

For the planned team workflow, see [PROJECT_WORKFLOW.md](PROJECT_WORKFLOW.md).

## Reference

Cortez, P., & Silva, A. (2008). *Using Data Mining to Predict Secondary School Student Performance*. In Proceedings of 5th Annual Future Business Technology Conference.
