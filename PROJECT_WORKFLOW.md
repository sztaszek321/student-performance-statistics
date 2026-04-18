# Project Workflow

This document describes the planned workflow for the first stage of the project: statistical analysis of the UCI Student Performance dataset.

## Team Workflow

The project should be developed in small, clear steps. Each step should produce either working code, a saved result, or a written interpretation that can later be used in the final report.

Recommended workflow:

1. Create or update a small part of the analysis.
2. Run `python analysis.py` and check that the script works.
3. Review the generated output or plots.
4. Write a short interpretation of the result.
5. Commit the finished change to Git.
6. Push the change to GitHub.

## Stage 1: Data Loading

Goal:

- load the dataset from the UCI repository,
- split the data into features and target variables,
- combine data into one DataFrame for easier analysis,
- verify the number of rows, columns, data types, and missing values.

Expected result:

- the script runs without errors,
- the dataset structure is clearly printed or summarized.

## Stage 2: Exploratory Data Analysis

Goal:

- describe the distribution of the final grade `G3`,
- calculate basic descriptive statistics,
- inspect selected categorical variables,
- check correlations between numeric variables and `G3`,
- prepare initial plots.

Expected result:

- basic tables and plots are created,
- the team understands which variables are promising for further analysis.

## Stage 3: Hypothesis Testing

Goal:

- choose several statistical hypotheses,
- define `H0` and `H1` for each test,
- select appropriate statistical tests,
- calculate test statistics and p-values,
- interpret the results at `alpha = 0.05`.

Example hypotheses:

- students with internet access at home have different final grades than students without internet access,
- students with past class failures have lower final grades,
- final grade differs depending on weekly study time,
- absences are related to final grade.

Expected result:

- each hypothesis has a clear test result and written interpretation.

## Stage 4: Multiple Regression

Goal:

- build a regression model for `G3`,
- use student, family, school, and lifestyle variables as predictors,
- exclude `G1` and `G2` from the main model,
- evaluate model quality and predictor significance.

Expected result:

- regression summary is available,
- important predictors are identified,
- coefficients are interpreted in context.

## Stage 5: Residual Analysis

Goal:

- analyze model residuals,
- check normality of residuals,
- check heteroscedasticity,
- inspect residual plots,
- identify possible outliers or influential observations.

Expected result:

- model assumptions are discussed,
- limitations of the regression model are clearly described.

## Stage 6: Report Preparation

Goal:

- move the most important results into the final report,
- describe methods and assumptions,
- include selected plots and tables,
- write conclusions based on hypothesis tests and regression analysis.

Expected result:

- the statistical part of the report is complete and consistent with the code.

## Git Rules

Recommended branch:

- `main` for stable project versions.

Recommended commit style:

- use short, descriptive commit messages,
- commit only working changes,
- avoid committing generated temporary files.

Example commit messages:

- `Add exploratory data summary`
- `Implement hypothesis tests`
- `Add regression model`
- `Add residual diagnostics`

## Definition of Done

A project stage is finished when:

- the code runs without errors,
- results are reproducible,
- outputs are understandable,
- interpretation is written,
- changes are committed and pushed to GitHub.
