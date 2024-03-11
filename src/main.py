from utils import formatted_operation, sort_by_data, load_file, filter_by_status
import os

print(os.getcwd())


def main(file, number_of_operations):
    data = load_file(file)
    data = filter_by_status(data)
    data = sort_by_data(data, number_of_operations)
    for operation in data:
        print(formatted_operation(operation))
        print()


main("../operations.json", 5)
