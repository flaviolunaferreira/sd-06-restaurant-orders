import csv
# How to find the max value in a dict 
# https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python#:~:text=values()%20to%20find%20the,max%20value%20of%20the%20dictionary.

def read_csv(path):
    with open(path) as file:
        content = list(csv.reader(file))
    return content


def most_requested_dish(requests, people):
    orders = {}
    for request in requests:
        if request[0] == people and request[1] not in orders:
            orders[request[1]] = 1
        elif request[0] == people:
            orders[request[1]] += 1
    return max(orders, key=orders.get)


def count_repeated_dish(requests, people, food):
    orders = 0
    for request in requests:
        if request[0] == people and request[1] == food:
            orders += 1
    return orders


def dishes_never_ordered(requests, people):
    all_dishes = set()
    dishes = set()
    for request in requests:
        all_dishes.add(request[1])
        if request[0] == people:
            dishes.add(request[1])
    return all_dishes.difference(dishes)


def days(requests, people):
    all_days = set()
    day = set()
    for request in requests:
        all_days.add(request[2])
        if request[0] == people:
            day.add(request[2])
    return all_days.difference(day)


def write_txt(path, data):
    with open(path, 'w') as file:
        for data in data:
            file.write(str(data) + '\n')


def analyze_log(path_to_file):
    data = []
    txt_path = 'data/mkt_campaign.txt'
    requests = read_csv(path_to_file)

    data.append(most_requested_dish(requests, 'maria'))
    data.append(count_repeated_dish(requests, 'arnaldo', 'hamburguer'))
    data.append(dishes_never_ordered(requests, 'joao'))
    data.append(days(requests, 'joao'))

    write_txt(txt_path, data)

    return data


if __name__ == "__main__":
    file = analyze_log('data/orders_1.csv')
    print(file)
