import csv

REPORT_PATH = "data/mkt_campaign.txt"

ROW_HEADERS = ["name", "dish", "weekday"]
REPORT_KEYS = ["clients", "dishes", "weekdays"]

NO_DISH = 0
DISH_INCREMENT = 1


def destructure(dict, *keys):
    return [dict[key] if key in dict else None for key in keys]


def build_report(path_to_file):
    report = {"weekdays": set(), "dishes": set(), "clients": {}}

    with open(path_to_file) as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=ROW_HEADERS)

        for row in reader:
            [name, dish, weekday] = destructure(row, *ROW_HEADERS)
            report["weekdays"].add(weekday)
            report["dishes"].add(dish)

            clients_report = report["clients"]
            new_order = {"dish": dish, "weekday": weekday}

            client_report = (
                clients_report[name]
                if name in clients_report
                else {
                    "orders": [],
                    "dish_count": {},
                    "weekdays": set(),
                }
            )

            client_dish_count = (
                client_report["dish_count"][dish]
                if dish in client_report["dish_count"]
                else NO_DISH
            )

            new_dish_count = client_dish_count + DISH_INCREMENT

            client_report["orders"].append(new_order)
            client_report["weekdays"].add(weekday)
            client_report["dish_count"][dish] = new_dish_count

            clients_report[name] = client_report

    return report


def analyze_log(path_to_file):
    report = build_report(path_to_file)

    [clients, dishes, weekdays] = destructure(report, *REPORT_KEYS)
    [maria, arnaldo, joao] = destructure(clients, "maria", "arnaldo", "joao")

    with open(REPORT_PATH, "w") as report_file:
        maria_dishes = maria["dish_count"]
        print(max(maria_dishes, key=maria_dishes.get), file=report_file)

        print(arnaldo["dish_count"]["hamburguer"], file=report_file)

        print(dishes.difference(set(joao["dish_count"])), file=report_file)

        print(weekdays.difference(joao["weekdays"]), file=report_file)
