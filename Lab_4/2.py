import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    V = []
    with open(INPUT_FILENAME, 'r') as input:
        reader = csv.DictReader(input)
        for row in reader:
            V.append(row)

    # TODO считать содержимое csv файла


    with open(OUTPUT_FILENAME, 'w') as write:
        json.dump(V, write, indent=4)
        # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")