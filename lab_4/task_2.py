import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open('input.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        # print(data)
        for rows in data:
            json_str = json.dumps(data, indent=4)
        # print(json_str)
    with open('output.json', 'w') as file:
        file.write(json_str)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
