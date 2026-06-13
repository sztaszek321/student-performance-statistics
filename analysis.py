import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo

from hypotheses import (
    run_all_hypothesis_tests,
    test_parent_education_vs_higher_education_plan,
    test_parent_education_vs_study_time_for_good_students,
    test_parent_status_vs_family_relationship,
    test_teacher_parent_vs_final_grade,
)
from regression import run_regression_analysis
from regression_ext import run_extended_regression_analysis
from queue_simulation import (
    plot_mean_waiting_time_histogram,
    run_simulation_experiments,
    summarize_simulation_results,
)


DATASET_ID = 320

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def load_student_performance_data():
    """Fetch the UCI Student Performance dataset."""
    student_performance = fetch_ucirepo(id=DATASET_ID)

    features = student_performance.data.features
    targets = student_performance.data.targets
    data = features.join(targets)

    return features, targets, data


def summarize_data(data):
    """Prepare basic summary tables for the notebook."""
    describe_summary = data.describe(include="all")

    value_summary = pd.DataFrame({
        "dtype": data.dtypes.astype(str),
        "unique": [data[column].nunique() for column in data.columns],
        "top": [data[column].mode().iloc[0] if not data[column].mode().empty else np.nan for column in data.columns],
        "mean": [
            round(data[column].mean(), 3) if pd.api.types.is_numeric_dtype(data[column]) else np.nan
            for column in data.columns
        ],
    })

    return describe_summary, value_summary


def print_basic_dataset_info(features, targets):
    """Print a short technical summary of the loaded data."""
    print("Features data:")
    print(features.info())

    print("\nTarget data:")
    print(targets.info())


def main():
    features, targets, data = load_student_performance_data()
    print_basic_dataset_info(features, targets)

    describe_summary, value_summary = summarize_data(data)
    print("\nOpis danych:")
    print(describe_summary)
    print("\nPodsumowanie kolumn:")
    print(value_summary)

    run_all_hypothesis_tests(data)
    run_regression_analysis(data)
    run_extended_regression_analysis(data)


if __name__ == "__main__":
    main()
