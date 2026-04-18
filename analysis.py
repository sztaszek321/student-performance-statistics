from ucimlrepo import fetch_ucirepo


DATASET_ID = 320


def load_student_performance_data():
    """Fetch the UCI Student Performance dataset."""
    student_performance = fetch_ucirepo(id=DATASET_ID)

    features = student_performance.data.features
    targets = student_performance.data.targets

    return features, targets


def print_basic_dataset_info(features, targets):
    """Print a short technical summary of the loaded data."""
    print("Features data:")
    print(features.info())

    print("\nTarget data:")
    print(targets.info())


def main():
    features, targets = load_student_performance_data()
    print_basic_dataset_info(features, targets)


if __name__ == "__main__":
    main()
