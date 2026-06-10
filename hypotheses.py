import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind


ALPHA = 0.05


def run_all_hypothesis_tests(data):
    """Run all planned hypothesis test templates."""
    test_teacher_parent_vs_final_grade(data)
    test_parent_status_vs_family_relationship(data)
    test_parent_education_vs_higher_education_plan(data)
    test_parent_education_vs_study_time_for_good_students(data)


def test_teacher_parent_vs_final_grade(data):
    """
    Hypothesis 1:
    Students with at least one parent working as a teacher achieve higher final
    grades than students without a teacher parent.

    Planned variables:
    - Mjob
    - Fjob
    - G3

    Planned derived variable:
    - teacher_parent = Mjob == "teacher" or Fjob == "teacher"

    Planned test:
    - independent samples t-test or Mann-Whitney U test
    """
    print("\nHypothesis 1: teacher parent vs final grade")
    print("H0: Parent as a teacher are independent of final grade.")
    print(
        "H1: Students with at least one parent working as a teacher are more likely "
        "to have higher final grade (G3)."
    )

    analysis_data = data.copy()
    analysis_data["teacher_parent"] = (
        (analysis_data["Mjob"] == 'teacher') | (analysis_data["Fjob"] == 'teacher')
    )

    teacher_parent_group = analysis_data.loc[analysis_data["teacher_parent"], "G3"]
    no_teacher_parent_group = analysis_data.loc[~analysis_data["teacher_parent"], "G3"]

    
    summary = analysis_data.groupby("teacher_parent")["G3"].agg(["count", "mean", "std"])

    t_statistic, p_value_two_sided = ttest_ind(
        teacher_parent_group,
        no_teacher_parent_group,
        equal_var=False,
    )

    if t_statistic > 0:
        p_value_one_sided = p_value_two_sided / 2
    else:
        p_value_one_sided = 1 - (p_value_two_sided / 2)

    print("\nGroup summary:")
    print(summary.round(4))
    print(f"\nT-statistic: {t_statistic:.4f}")
    print(f"One-sided p-value: {p_value_one_sided:.4f}")

    if p_value_one_sided < ALPHA:
        print(
            "Result: reject H0. Students with at least one teacher parent "
            "have a significantly higher mean final grade."
        )
    else:
        print(
            "Result: fail to reject H0. There is not enough evidence to conclude "
            "that students with at least one teacher parent have a higher mean final grade."
        )


def test_parent_status_vs_family_relationship(data):
    """
    Hypothesis 2:
    Students whose parents live apart report weaker family relationships than
    students whose parents live together.

    Planned variables:
    - Pstatus
    - famrel

    Planned test:
    - Mann-Whitney U test
    """
    print("\nHypothesis 2: parent status vs family relationship")
    print(
        "H0: Family relationship scores are the same for students whose parents "
        "live together and apart."
    )
    print(
        "H1: Students whose parents live apart report lower family relationship "
        "scores."
    )

    analysis_data = data.copy()
    parents_together_group = analysis_data.loc[
        analysis_data["Pstatus"] == "T", "famrel"
    ]
    parents_apart_group = analysis_data.loc[
        analysis_data["Pstatus"] == "A", "famrel"
    ]

    summary = analysis_data.groupby("Pstatus")["famrel"].agg(
        ["count", "mean", "median", "std"]
    )

    u_statistic, p_value_two_sided = mannwhitneyu(
        parents_apart_group,
        parents_together_group,
        alternative="two-sided",
    )

    if parents_apart_group.median() < parents_together_group.median():
        p_value_one_sided = p_value_two_sided / 2
    else:
        p_value_one_sided = 1 - (p_value_two_sided / 2)

    print("\nGroup summary:")
    print(summary.round(4))
    print(f"\nMann-Whitney U statistic: {u_statistic:.4f}")
    print(f"One-sided p-value: {p_value_one_sided:.4f}")

    if p_value_one_sided < ALPHA:
        print(
            "Result: reject H0. Students whose parents live apart report "
            "significantly weaker family relationships."
        )
    else:
        print(
            "Result: fail to reject H0. There is not enough evidence to conclude "
            "that students whose parents live apart report weaker family "
            "relationships."
        )


def test_parent_education_vs_higher_education_plan(data):
    """
    Hypothesis 3:
    Students with at least one highly educated parent are more likely to want to
    pursue higher education.

    Planned variables:
    - Medu
    - Fedu
    - higher

    Planned derived variable:
    - highly_educated_parent = Medu == 4 or Fedu == 4

    Planned test:
    - chi-square test of independence
    """
    print("\nHypothesis 3: parent education vs higher education plan")
    print("H0: Higher education plans are independent of parental education.")
    print(
        "H1: Students with at least one highly educated parent are more likely "
        "to want to pursue higher education."
    )

    analysis_data = data.copy()
    analysis_data["highly_educated_parent"] = (
        (analysis_data["Medu"] == 4) | (analysis_data["Fedu"] == 4)
    )

    contingency_table = pd.crosstab(
        analysis_data["highly_educated_parent"],
        analysis_data["higher"],
    )

    chi2_statistic, p_value, degrees_of_freedom, _ = chi2_contingency(
        contingency_table
    )
    higher_education_rates = pd.crosstab(
        analysis_data["highly_educated_parent"],
        analysis_data["higher"],
        normalize="index",
    )

    print("\nContingency table:")
    print(contingency_table)
    print("\nHigher education plan rates by group:")
    print((higher_education_rates * 100).round(2))
    print(f"\nChi-square statistic: {chi2_statistic:.4f}")
    print(f"Degrees of freedom: {degrees_of_freedom}")
    print(f"P-value: {p_value:.4f}")

    if p_value < ALPHA:
        print(
            "Result: reject H0. There is a statistically significant "
            "relationship between parental education and higher education plans."
        )
    else:
        print(
            "Result: fail to reject H0. There is not enough evidence to confirm "
            "a statistically significant relationship between parental education "
            "and higher education plans."
        )


def test_parent_education_vs_study_time_for_good_students(data):
    """
    Hypothesis 4:
    Among students achieving good final grades, students with at least one
    highly educated parent report lower study time than students without a
    highly educated parent.

    Planned variables:
    - Medu
    - Fedu
    - studytime
    - G3

    Planned derived variables:
    - highly_educated_parent = Medu == 4 or Fedu == 4
    - good_grade = G3 >= selected threshold, for example 14

    Planned test:
    - Mann-Whitney U test on the filtered group of good students
    """
    print("\nHypothesis 4: parent education vs study time for good students")
    print(
        "H0: Among students with good final grades, study time is the same "
        "regardless of parental education."
    )
    print(
        "H1: Among students with good final grades, students with at least one "
        "highly educated parent report lower study time."
    )

    analysis_data = data.copy()
    analysis_data["highly_educated_parent"] = (
        (analysis_data["Medu"] == 4) | (analysis_data["Fedu"] == 4)
    )
    good_students = analysis_data.loc[analysis_data["G3"] >= 14].copy()

    highly_educated_parent_group = good_students.loc[
        good_students["highly_educated_parent"], "studytime"
    ]
    no_highly_educated_parent_group = good_students.loc[
        ~good_students["highly_educated_parent"], "studytime"
    ]

    summary = good_students.groupby("highly_educated_parent")["studytime"].agg(
        ["count", "mean", "median", "std"]
    )

    u_statistic, p_value_two_sided = mannwhitneyu(
        highly_educated_parent_group,
        no_highly_educated_parent_group,
        alternative="two-sided",
    )

    if highly_educated_parent_group.median() < no_highly_educated_parent_group.median():
        p_value_one_sided = p_value_two_sided / 2
    else:
        p_value_one_sided = 1 - (p_value_two_sided / 2)

    print("\nGood student threshold: G3 >= 14")
    print("\nGroup summary:")
    print(summary.round(4))
    print(f"\nMann-Whitney U statistic: {u_statistic:.4f}")
    print(f"One-sided p-value: {p_value_one_sided:.4f}")

    if p_value_one_sided < ALPHA:
        print(
            "Result: reject H0. Among students with good final grades, those "
            "with at least one highly educated parent report significantly lower "
            "study time."
        )
    else:
        print(
            "Result: fail to reject H0. There is not enough evidence to conclude "
            "that, among students with good final grades, those with at least "
            "one highly educated parent report lower study time."
        )
