import csv


def analyze_log(path_to_file):
    data_json = csv_to_json(path_to_file)
    maria = get_maria_most_requested(data_json)
    arnaldo = get_arnaldo_hamburguer_count(data_json)
    order_joao_never = get_joao_never_did(data_json, 'order')
    day_joao_never = get_joao_never_did(data_json, 'day')

    file = open('data/mkt_campaign.txt', mode='w')

    file.write(maria + '\n')
    file.write(str(arnaldo) + '\n')
    file.write(str(order_joao_never) + '\n')
    file.write(str(day_joao_never))
    file.close()


def csv_to_json(filename):
    if '.csv' in filename:
        with open(filename) as file:
            content = csv.DictReader(file)
            content.fieldnames = ['name'] + ['order'] + ['day']
            jsonFormat = []
            for info in content:
                jsonFormat.append(info)
            return jsonFormat
    else:
        raise FileNotFoundError(f"No such file or directory: '{filename}'")


def get_maria_most_requested(order_data):
    count = {}
    most_requested = {'most_repet': '', 'repet': 1}
    for order in order_data:
        is_maria = order['name'] == 'maria'
        if is_maria and order['order'] in count.keys():
            count[order['order']] += 1
        if is_maria and order['order'] not in count.keys():
            count[order['order']] = 1
        if is_maria and count[order['order']] > most_requested['repet']:
            most_requested = {
                'most_repet': order['order'],
                'repet': count[order['order']]
            }

    return most_requested['most_repet']


def get_arnaldo_hamburguer_count(order_data):
    count = 0
    for order in order_data:
        if order['name'] == 'arnaldo' and order['order'] == 'hamburguer':
            count += 1

    return count


def get_joao_never_did(order_data, parameter):
    all_list = set()
    joao_list = set()
    for order in order_data:
        if order[parameter] not in all_list:
            all_list.add(order[parameter])
        if order['name'] == 'joao' and order[parameter] not in joao_list:
            joao_list.add(order[parameter])

    return all_list.difference(joao_list)
