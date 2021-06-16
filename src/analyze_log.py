from src.utils.report_generator import build_report
from src.utils.destructure import destructure

REPORT_PATH = "data/mkt_campaign.txt"

REPORT_KEYS = ["clients", "dishes", "weekdays"]


def analyze_log(path_to_file):
    report = build_report(path_to_file)

    [clients, dishes, weekdays] = destructure(report, *REPORT_KEYS)
    [maria, arnaldo, joao] = destructure(clients, "maria", "arnaldo", "joao")

    unique_days = set(weekdays.keys())

    with open(REPORT_PATH, "w") as report_file:
        maria_dishes = maria["dish_count"]
        print(max(maria_dishes, key=maria_dishes.get), file=report_file)

        print(arnaldo["dish_count"]["hamburguer"], file=report_file)

        print(dishes.difference(set(joao["dish_count"])), file=report_file)

        print(unique_days.difference(joao["weekdays"]), file=report_file)
