import re

with open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [re.findall('[0-9]+', line.strip()) for line in raw_data if line != '\n']


def first_star(data):
    result = 0

    arcade_machines = []

    for i, line in enumerate(data):
        if i % 3 == 0:
            A_button = [int(i) for i in line]
            B_button = [int(i) for i in data[i + 1]]
            Prize = [int(i) for i in data[i + 2]]
            arcade_machines.append({'A': A_button, 'B': B_button, 'Prize': Prize})

    for i in arcade_machines:
        print(i)



    print(f'first_star {result=}')


def second_star(data):
    result = 0
    print(f'second_star {result=}')


if __name__ == '__main__':
    first_star(data)
    second_star(data)
