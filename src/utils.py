import csv


def reading_file_csv(path_to_file):
    """# ler arquivo csv"""
    with open(path_to_file) as file:
        read = csv.reader(file)
        text = [item for item in read]
    return text


def writing_file_txt(data_answers, answers):
    """# guardar as respostas"""
    with open(data_answers, "w") as file:
        for item in answers:
            file.write(str(item) + "\n")
