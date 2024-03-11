import json


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_by_status(dictionary_list):
    '''Фильтрация списка словарей по статусу '''
    filter_status_list = []
    for operations in dictionary_list:
        if "state" in operations and operations["state"] == "EXECUTED":
            filter_status_list.append(operations)
    return filter_status_list


def sort_by_data(dictionary_list, number_of_operations):
    '''Сортировка словарей списка по дате'''
    dictionary_list = sorted(dictionary_list, key=lambda x: x["date"], reverse=True)
    return dictionary_list[:number_of_operations]