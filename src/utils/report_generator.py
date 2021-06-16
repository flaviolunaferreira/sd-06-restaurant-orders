import csv

from src.utils.destructure import destructure

ROW_HEADERS = ["name", "dish", "weekday"]

ZERO = 0
COUNT_INCREMENT = 1
FIRST_COUNT = 1


def build_report(path_to_file):
    report = {"weekdays": {}, "dishes": set(), "clients": {}}

    with open(path_to_file) as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=ROW_HEADERS)

        for row in reader:
            [name, dish, weekday] = destructure(row, *ROW_HEADERS)
            report["dishes"].add(dish)

            clients_report = report["clients"]

            weekday_report = report["weekdays"]
            weekday_report[weekday] = (
                weekday_report[weekday] + COUNT_INCREMENT
                if weekday in weekday_report
                else FIRST_COUNT
            )

            client_report = (
                clients_report[name]
                if name in clients_report
                else {
                    "orders": [],
                    "dish_count": {},
                    "weekdays": set(),
                }
            )

            client_dish_track = client_report["dish_count"]
            client_dish_count = (
                client_dish_track[dish] if dish in client_dish_track else ZERO
            )

            new_dish_count = client_dish_count + COUNT_INCREMENT
            client_report["dish_count"][dish] = new_dish_count

            new_order = {"dish": dish, "weekday": weekday}
            client_report["orders"].append(new_order)

            client_report["weekdays"].add(weekday)

            clients_report[name] = client_report

    return report
