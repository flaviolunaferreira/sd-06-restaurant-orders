import csv


def read_file(path_to_file):
    with open(path_to_file) as file:
        read = csv.reader(file)
        text = [item for item in read]
    return text


def write_file(data_answers, answers):
    with open(data_answers) as file:
        for item in answers:
            file.write(str(item) + "\n")
