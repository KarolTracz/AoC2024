import re

with open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [re.findall('[0-9]+', line.strip()) for line in raw_data if line != '\n']


def first_star(data):
    result = 0

    print(data)

    arcade_machines = {}

    for i, line in enumerate(data):
        if i % 3 == 0:
            arcade_machines[i//3] = {'A': line, 'B': data[i+1], 'Prize': data[i+2]}

    print(arcade_machines)

    for k, v in arcade_machines.items():
        print(k, v)

    print(f'first_star {result=}')


def second_star(data):
    result = 0
    print(f'second_star {result=}')


if __name__ == '__main__':
    first_star(data)
    second_star(data)
