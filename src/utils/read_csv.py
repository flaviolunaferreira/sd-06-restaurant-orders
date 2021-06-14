import csv


def read_csv(path):
    if path.split(".", 1)[1] != "csv":
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    with open(path) as file:
        csv_file = csv.reader(file)
        return list(csv_file)
