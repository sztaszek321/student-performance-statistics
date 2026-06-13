import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import shapiro
from statsmodels.api import add_constant
from statsmodels.stats.diagnostic import het_breuschpagan, linear_rainbow
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson


EXTENDED_REGRESSION_FORMULA = (
    "G3 ~ Medu + Fedu + traveltime + studytime + failures + "
    "C(schoolsup) + C(famsup) + C(paid) + C(activities) + C(higher) + "
    "absences + freetime + Walc + Dalc + famrel"
)


EXTENDED_REGRESSION_COLUMNS = [
    "G3",
    "Medu",
    "Fedu",
    "traveltime",
    "studytime",
    "failures",
    "schoolsup",
    "famsup",
    "paid",
    "activities",
    "higher",
    "absences",
    "freetime",
    "Walc",
    "Dalc",
    "famrel",
]


EXTENDED_PREDICTOR_COLUMNS = [
    "Medu",
    "Fedu",
    "traveltime",
    "studytime",
    "failures",
    "schoolsup",
    "famsup",
    "paid",
    "activities",
    "higher",
    "absences",
    "freetime",
    "Walc",
    "Dalc",
    "famrel",
]


def run_extended_regression_analysis(data):
    regression_data = prepare_extended_regression_data(data)
    model = build_extended_regression_model(regression_data)

    print_model_summary(model, regression_data)
    print_coefficients(model)
    print_vif(regression_data)
    analyze_residuals(model)


def prepare_extended_regression_data(data):
    regression_data = data[EXTENDED_REGRESSION_COLUMNS].dropna().copy()
    return regression_data


def build_extended_regression_model(data):
    return smf.ols(EXTENDED_REGRESSION_FORMULA, data=data).fit()


def print_model_summary(model, data):
    print("\nREGRESJA WIELORAKA - MODEL ROZSZERZONY")

    print(f"\nLiczba obserwacji: {len(data)}")
    print("Formuła modelu:")
    print(EXTENDED_REGRESSION_FORMULA)

    print("\nOcena dopasowania modelu:")
    print(f"R2: {model.rsquared:.4f}")
    print(f"Skorygowane R2: {model.rsquared_adj:.4f}")
    print(f"AIC: {model.aic:.4f}")
    print(f"BIC: {model.bic:.4f}")
    print(f"p-value testu F: {model.f_pvalue:.4f}")


def print_coefficients(model):
    coefficient_table = pd.DataFrame({
        "coef": model.params,
        "p_value": model.pvalues,
    })
    coefficient_table["istotne_0_05"] = coefficient_table["p_value"] < 0.05

    print("\nWspółczynniki modelu:")
    print(coefficient_table.round(4).to_string())


def prepare_vif_data(data):
    vif_data = pd.get_dummies(
        data[EXTENDED_PREDICTOR_COLUMNS],
        drop_first=True,
        dtype=float,
    )
    vif_data = add_constant(vif_data)
    return vif_data


def print_vif(data):
    vif_data = prepare_vif_data(data)

    vif_results = pd.DataFrame({
        "feature": vif_data.columns,
        "VIF": [
            variance_inflation_factor(vif_data.values, i)
            for i in range(vif_data.shape[1])
        ],
    })

    print("\nVIF - współliniowość zmiennych:")
    print(vif_results.round(4).to_string(index=False))


def analyze_residuals(model):
    residuals = model.resid

    shapiro_statistic, shapiro_p_value = shapiro(residuals)
    bp_statistic, bp_p_value, _, _ = het_breuschpagan(residuals, model.model.exog)
    dw_statistic = durbin_watson(residuals)
    rainbow_statistic, rainbow_p_value = linear_rainbow(model)

    print("\nDiagnostyka reszt:")
    print(f"Shapiro-Wilk p-value: {shapiro_p_value:.4f}")
    print(f"Breusch-Pagan p-value: {bp_p_value:.4f}")
    print(f"Durbin-Watson: {dw_statistic:.4f}")
    print(f"Rainbow p-value: {rainbow_p_value:.4f}")