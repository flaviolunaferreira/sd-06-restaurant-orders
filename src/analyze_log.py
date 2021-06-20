import csv
from collections import Counter


def convert_to_dict(path_to_file):
    with open(path_to_file, 'r') as csv_file:
        headers = ['name', 'order', 'day']
        result_dict = csv.DictReader(csv_file, fieldnames=headers)
        clients = []
        [clients.append(data_row) for data_row in result_dict]
        return clients


def most_frequent_order(client_name, clients_data):
    client_order = [
        client['order'] for client
        in clients_data if client['name'] == client_name
    ]
    ordered_times = Counter(client_order)
    results = ordered_times.most_common(1)[0][0]
    return results


def ordered_times(client_name, clients_data, menu_item):
    client_order = [
        client['order'] for client
        in clients_data if client['name'] == client_name
    ]
    ordered_times = Counter(client_order)
    return ordered_times.get(menu_item)


def never_orderd(client_name, clients_data):
    orders_set = {client['order'] for client in clients_data}
    orders_by_client = {
        client['order'] for client
        in clients_data if client['name'] == client_name
    }
    return orders_set.symmetric_difference(orders_by_client)


def never_show_day(client_name, clients_data):
    days_set = {client['day'] for client in clients_data}
    days_by_client = {
        client['day'] for client
        in clients_data if client['name'] == client_name
    }
    return days_set.symmetric_difference(days_by_client)


def analyze_log(path_to_file):
    if path_to_file.endswith('.csv'):
        clients_data = convert_to_dict(path_to_file)
        most_frequent_maria_orders = most_frequent_order('maria', clients_data)
        arnaldo_orders = ordered_times('arnaldo', clients_data, 'hamburger')
        never_orderd_by_joao = never_orderd('joao', clients_data)
        joao_s_never_show_day = never_show_day('jaoao', clients_data)
        rows = [
            f'{most_frequent_maria_orders}\n',
            f'{arnaldo_orders}\n',
            f'{never_orderd_by_joao}\n',
            f'{joao_s_never_show_day}',
        ]
        with open('data/mkt_campaign.txt', 'w') as txt_file:
            txt_file.writelines(rows)
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


if __name__ == '__main__':
    path = 'data/orders_3.csv'
    analyze_log(path)
