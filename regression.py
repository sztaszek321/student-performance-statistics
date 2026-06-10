import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import het_breuschpagan, linear_rainbow
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson


REGRESSION_FORMULA = (
    "G3 ~ studytime + failures + absences + Medu + Fedu + "
    "traveltime + C(internet) + C(schoolsup) + C(higher)"
)


def run_regression_analysis(data):
    """Run the first working version of the multiple regression analysis."""
    print("\nRegression analysis")

    regression_data = prepare_regression_data(data)
    model = build_main_regression_model(regression_data)

    print_model_summary(model, regression_data)
    print_model_selection_metrics(model)
    print_vif(regression_data)
    analyze_residuals(model)


def prepare_regression_data(data):
    """Select and clean the columns used in the main regression model."""
    regression_columns = [
        "G3",
        "studytime",
        "failures",
        "absences",
        "Medu",
        "Fedu",
        "traveltime",
        "internet",
        "schoolsup",
        "higher",
    ]

    regression_data = data[regression_columns].dropna().copy()
    return regression_data


def build_main_regression_model(data):
    """Build the main OLS multiple regression model."""
    return smf.ols(REGRESSION_FORMULA, data=data).fit()


def print_model_summary(model, data):
    """Print the core regression output."""
    print(f"\nObservations used in regression: {len(data)}")
    print("\nRegression formula:")
    print(REGRESSION_FORMULA)
    print("\nModel summary:")
    print(model.summary())


def print_model_selection_metrics(model):
    """Print basic model comparison metrics."""
    print("\nModel selection metrics:")
    print(f"AIC: {model.aic:.4f}")
    print(f"BIC: {model.bic:.4f}")


def print_vif(data):
    """Print variance inflation factors for the predictors."""
    vif_data = pd.get_dummies(
        data[
            [
                "studytime",
                "failures",
                "absences",
                "Medu",
                "Fedu",
                "traveltime",
                "internet",
                "schoolsup",
                "higher",
            ]
        ],
        drop_first=True,
    )

    vif_data = sm.add_constant(vif_data)

    vif_results = pd.DataFrame(
        {
            "feature": vif_data.columns,
            "VIF": [
                variance_inflation_factor(vif_data.values, i)
                for i in range(vif_data.shape[1])
            ],
        }
    )

    print("\nVariance Inflation Factors:")
    print(vif_results.round(4).to_string(index=False))


def analyze_residuals(model):
    """Print basic residual diagnostics."""
    residuals = model.resid

    shapiro_statistic, shapiro_p_value = shapiro(residuals)
    bp_statistic, bp_p_value, _, _ = het_breuschpagan(residuals, model.model.exog)
    dw_statistic = durbin_watson(residuals)
    rainbow_statistic, rainbow_p_value = linear_rainbow(model)

    print("\nResidual diagnostics:")
    print(f"Shapiro-Wilk statistic: {shapiro_statistic:.4f}")
    print(f"Shapiro-Wilk p-value: {shapiro_p_value:.4f}")
    print(f"Breusch-Pagan statistic: {bp_statistic:.4f}")
    print(f"Breusch-Pagan p-value: {bp_p_value:.4f}")
    print(f"Durbin-Watson statistic: {dw_statistic:.4f}")
    print(f"Rainbow statistic: {rainbow_statistic:.4f}")
    print(f"Rainbow p-value: {rainbow_p_value:.4f}")
