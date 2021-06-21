import csv


class HandleCSV:
    @classmethod
    def read_csv_file(cls, path):
        with open(path) as file:
            return list(csv.reader(file))

    @classmethod
    def write_text(cls, path, data):
        with open(path, "w") as campaign_file:
            campaign_file.write(data)
