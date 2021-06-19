#!/usr/bin/env python3
import csv
from collections import Counter

path_to_file = "data/orders_1.csv"
path_to_write_file = "data/mkt_campaign.txt"
available_dishes = ["hamburguer", "pizza", "coxinha", "misto-quente"]
opening_days = ["segunda-feira", "terça-feira", "sabado"]


def txt_writer(data_to_write, file_to_write):
    with open(file_to_write, 'a', encoding='utf-8') as file:
        file.write(data_to_write)
        file.write("\n")


def csv_to_dict(file_to_read):
    with open(file_to_read, 'r') as file:
        reader = csv.reader(file)
        restaurant_data = [{
            "name": row[0],
            "food": row[1],
            "day": row[2]
        } for row in reader]
        return restaurant_data


def get_person_food_data(person_name, data_file):
    person_data = []
    for data in data_file:
        if data["name"] == person_name:
            person_data.append(data["food"])
    return person_data


def get_person_frequency_data(person_name, data_file):
    person_data = []
    for data in data_file:
        if data["name"] == person_name:
            person_data.append(data["day"])
    return person_data


def most_ordered_dish_by_person(person_food_data):
    return (Counter(person_food_data).most_common(1)[0][0])


def count_dish_orders(person_food_data, dish):
    return Counter(person_food_data)[dish]


def never_ordered_dishes(person_food_data, available_dishes):
    for food in person_food_data:
        if food in available_dishes:
            available_dishes.remove(food)
    return set(available_dishes)


def days_person_never_attended(person_frequency_data, opening_days):
    for day in person_frequency_data:
        if day in opening_days:
            opening_days.remove(day)
    return set(opening_days)


def analyze_log(path_to_file):
    dict_restaurant_data = csv_to_dict(path_to_file)

    maria_food_data = get_person_food_data("maria", dict_restaurant_data)
    maria_most_ordered = most_ordered_dish_by_person(maria_food_data)

    arnaldo_food_data = get_person_food_data(
        "arnaldo", dict_restaurant_data)
    arnaldo_hamburguer_orders = count_dish_orders(
        arnaldo_food_data, 'hamburguer')

    joao_food_data = get_person_food_data(
        "joao", dict_restaurant_data)
    joao_frequency_data = get_person_frequency_data(
        "joao", dict_restaurant_data)
    joao_never_ordered = never_ordered_dishes(
        joao_food_data, available_dishes)
    joao_never_went = days_person_never_attended(
        joao_frequency_data, opening_days)

    txt_writer(str(maria_most_ordered), path_to_write_file)
    txt_writer(str(arnaldo_hamburguer_orders), path_to_write_file)
    txt_writer(str(joao_never_ordered), path_to_write_file)
    txt_writer(str(joao_never_went), path_to_write_file)
