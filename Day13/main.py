import re

with open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [re.findall('[0-9]+', line.strip()) for line in raw_data if line != '\n']


def first_star(data):
    result = 0

    arcade_machines = []

    for machine, line in enumerate(data):
        if machine % 3 == 0:
            a_button = [int(i) for i in line]
            b_button = [int(i) for i in data[machine + 1]]
            prize = [int(i) for i in data[machine + 2]]
            arcade_machines.append({'A': a_button, 'B': b_button, 'Prize': prize})

    for machine in arcade_machines:
        tokens = 0

        a_x, a_y = machine['A']
        b_x, b_y = machine['B']
        goal_x, goal_y = machine['Prize']

        for a_press in range(101):
            for b_press in range(101):
                if a_x * a_press + b_x * b_press == goal_x and a_y * a_press + b_y * b_press == goal_y:
                    print(f'{a_press=} {b_press=} {machine=}')
                    tokens = 3 * a_press + b_press
                    break
                    # print(f'{A_x} * {A_press} + {B_x} * {B_press} == {goal_x}')
                    # print(f'{A_y} * {A_press} + {B_y} * {B_press} == {goal_y}')
        result += tokens

    print(f'first_star {result=}')


def second_star(data):
    result = 0
    print(f'second_star {result=}')


if __name__ == '__main__':
    first_star(data)
    second_star(data)
