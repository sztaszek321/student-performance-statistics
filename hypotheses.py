import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind


ALPHA = 0.05


def print_decision(p_value, reject_text, keep_text):
    print(f"p-value = {p_value:.4f}")

    if p_value < ALPHA:
        print(f"Decyzja: p < {ALPHA}, odrzucamy H0.")
        print(f"Wniosek: {reject_text}")
    else:
        print(f"Decyzja: p >= {ALPHA}, brak podstaw do odrzucenia H0.")
        print(f"Wniosek: {keep_text}")


def has_two_groups(first_group, second_group):
    return len(first_group) > 0 and len(second_group) > 0


def run_all_hypothesis_tests(data):
    test_teacher_parent_vs_final_grade(data)
    test_parent_status_vs_family_relationship(data)
    test_parent_education_vs_higher_education_plan(data)
    test_parent_education_vs_study_time_for_good_students(data)


def test_teacher_parent_vs_final_grade(data):
    print("\nHIPOTEZA 1")
    print("Czy uczniowie z rodzicem nauczycielem mają wyższe oceny końcowe G3?")
    print("Test: test t Welcha dla dwóch niezależnych grup, jednostronny.")

    analysis_data = data.copy()
    analysis_data["teacher_parent"] = (
        (analysis_data["Mjob"] == "teacher") | (analysis_data["Fjob"] == "teacher")
    )
    analysis_data["group"] = analysis_data["teacher_parent"].map({
        True: "rodzic nauczyciel",
        False: "brak rodzica nauczyciela",
    })

    teacher_parent_group = analysis_data.loc[analysis_data["teacher_parent"], "G3"]
    no_teacher_parent_group = analysis_data.loc[~analysis_data["teacher_parent"], "G3"]

    summary = analysis_data.groupby("group")["G3"].agg(["count", "mean", "std"])
    print("\nPodsumowanie grup:")
    print(summary.round(3))

    if not has_two_groups(teacher_parent_group, no_teacher_parent_group):
        print("\nNie można wykonać testu, bo jedna z grup jest pusta.")
        return

    t_statistic, p_value_two_sided = ttest_ind(
        teacher_parent_group,
        no_teacher_parent_group,
        equal_var=False,
    )

    if t_statistic > 0:
        p_value_one_sided = p_value_two_sided / 2
    else:
        p_value_one_sided = 1 - (p_value_two_sided / 2)

    print(f"\nStatystyka t = {t_statistic:.4f}")
    print_decision(
        p_value_one_sided,
        "uczniowie z co najmniej jednym rodzicem nauczycielem mają istotnie wyższą średnią ocenę G3.",
        "nie ma wystarczających dowodów, że rodzic nauczyciel oznacza wyższą ocenę G3.",
    )


def test_parent_status_vs_family_relationship(data):
    print("\nHIPOTEZA 2")
    print("Czy uczniowie, których rodzice mieszkają osobno, gorzej oceniają relacje rodzinne?")
    print("Test: U Manna-Whitneya dla dwóch niezależnych grup, jednostronny.")

    analysis_data = data.copy()
    analysis_data["group"] = analysis_data["Pstatus"].map({
        "A": "rodzice osobno",
        "T": "rodzice razem",
    })

    parents_apart_group = analysis_data.loc[analysis_data["Pstatus"] == "A", "famrel"]
    parents_together_group = analysis_data.loc[analysis_data["Pstatus"] == "T", "famrel"]

    summary = analysis_data.groupby("group")["famrel"].agg(["count", "mean", "median", "std"])
    print("\nPodsumowanie grup:")
    print(summary.round(3))

    if not has_two_groups(parents_apart_group, parents_together_group):
        print("\nNie można wykonać testu, bo jedna z grup jest pusta.")
        return

    u_statistic, p_value = mannwhitneyu(
        parents_apart_group,
        parents_together_group,
        alternative="less",
    )

    print(f"\nStatystyka U = {u_statistic:.4f}")
    print_decision(
        p_value,
        "uczniowie, których rodzice mieszkają osobno, istotnie słabiej oceniają relacje rodzinne.",
        "nie ma wystarczających dowodów, że mieszkanie rodziców osobno obniża ocenę relacji rodzinnych.",
    )


def test_parent_education_vs_higher_education_plan(data):
    print("\nHIPOTEZA 3")
    print("Czy wyższe wykształcenie rodzica wiąże się z planem dalszej edukacji ucznia?")
    print("Test: chi-kwadrat niezależności dla tabeli kontyngencji.")

    analysis_data = data.copy()
    analysis_data["highly_educated_parent"] = (
        (analysis_data["Medu"] == 4) | (analysis_data["Fedu"] == 4)
    )
    analysis_data["group"] = analysis_data["highly_educated_parent"].map({
        True: "min. jeden rodzic wyższe",
        False: "brak rodzica z wyższym",
    })

    contingency_table = pd.crosstab(analysis_data["group"], analysis_data["higher"])
    rates = pd.crosstab(
        analysis_data["group"],
        analysis_data["higher"],
        normalize="index",
    )

    result_table = contingency_table.copy()

    if "no" in rates.columns:
        result_table["no_%"] = (rates["no"] * 100).round(2).astype(str) + "%"

    if "yes" in rates.columns:
        result_table["yes_%"] = (rates["yes"] * 100).round(2).astype(str) + "%"

    print("\nTabela liczebności i odsetków:")
    print(result_table)

    if contingency_table.shape[0] < 2 or contingency_table.shape[1] < 2:
        print("\nNie można wykonać testu, bo tabela nie ma dwóch porównywanych grup lub dwóch odpowiedzi.")
        return

    chi2_statistic, p_value, degrees_of_freedom, _ = chi2_contingency(contingency_table)

    print(f"\nStatystyka chi2 = {chi2_statistic:.4f}")
    print(f"Stopnie swobody = {degrees_of_freedom}")
    print_decision(
        p_value,
        "istnieje istotna zależność między wykształceniem rodziców a planem dalszej edukacji.",
        "nie ma wystarczających dowodów na zależność między wykształceniem rodziców a planem dalszej edukacji.",
    )


def test_parent_education_vs_study_time_for_good_students(data):
    print("\nHIPOTEZA 4")
    print("Czy dobrzy uczniowie z wysoko wykształconym rodzicem uczą się krócej?")
    print("Test: U Manna-Whitneya dla dwóch niezależnych grup, jednostronny.")
    print("Próg dobrego wyniku: G3 >= 14.")

    analysis_data = data.copy()
    analysis_data["highly_educated_parent"] = (
        (analysis_data["Medu"] == 4) | (analysis_data["Fedu"] == 4)
    )
    good_students = analysis_data.loc[analysis_data["G3"] >= 14].copy()
    good_students["group"] = good_students["highly_educated_parent"].map({
        True: "min. jeden rodzic wyższe",
        False: "brak rodzica z wyższym",
    })

    highly_educated_parent_group = good_students.loc[
        good_students["highly_educated_parent"], "studytime"
    ]
    no_highly_educated_parent_group = good_students.loc[
        ~good_students["highly_educated_parent"], "studytime"
    ]

    summary = good_students.groupby("group")["studytime"].agg(["count", "mean", "median", "std"])
    print("\nPodsumowanie grup:")
    print(summary.round(3))

    if not has_two_groups(highly_educated_parent_group, no_highly_educated_parent_group):
        print("\nNie można wykonać testu, bo jedna z grup jest pusta po filtrze G3 >= 14.")
        return

    u_statistic, p_value = mannwhitneyu(
        highly_educated_parent_group,
        no_highly_educated_parent_group,
        alternative="less",
    )

    print(f"\nStatystyka U = {u_statistic:.4f}")
    print_decision(
        p_value,
        "wśród dobrych uczniów osoby z wysoko wykształconym rodzicem deklarują istotnie krótszy czas nauki.",
        "nie ma wystarczających dowodów, że dobrzy uczniowie z wysoko wykształconym rodzicem uczą się krócej.",
    )