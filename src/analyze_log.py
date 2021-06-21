from src.report_helpers.get_customer_most_ordered_food import (
    get_customer_most_ordered_food,
)
from src.report_helpers.generate_orders_report import generate_orders_report
from src.report_helpers.get_customer_food_quantity import (
    get_customer_food_quantity,
)
from src.report_helpers.get_customer_non_ordered_foods import (
    get_customer_non_ordered_foods,
)
from src.report_helpers.get_customer_days_without_going import (
    get_customer_days_without_going,
)


def analyze_log(path_to_file):
    if not path_to_file.lower().endswith(".csv"):
        raise FileNotFoundError(
            "No such file or directory: " f"'{path_to_file}'"
        )
    try:
        orders_report = generate_orders_report(path_to_file)
    except OSError:
        raise FileNotFoundError(
            "No such file or directory: " f"'{path_to_file}'"
        )

    maria_most_ordered_food = get_customer_most_ordered_food(
        "maria", orders_report
    )
    arnaldo_hamburgers_quantity = str(
        get_customer_food_quantity("arnaldo", "hamburguer", orders_report)
    )
    joao_never_ordered = str(
        get_customer_non_ordered_foods("joao", orders_report)
    )
    joao_never_went = str(
        get_customer_days_without_going("joao", orders_report)
    )

    with open("data/mkt_campaign.txt", "w") as file:
        print(maria_most_ordered_food, file=file)
        print(arnaldo_hamburgers_quantity, file=file)
        print(joao_never_ordered, file=file)
        print(joao_never_went, file=file)
    return orders_report
