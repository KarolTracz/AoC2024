from collections import Counter

with open('input.txt', 'r') as f:
# with open('test_input.txt', 'r') as f:
    raw_input = f.readlines()

new_test_input = raw_input.copy()

def first_star():
    result = 0
    start_x, start_y = find_asterix(raw_input)
    position = [start_y, start_x]
    directions = ('u', 'r', 'd', 'l')
    while True:
        for direction in directions:
            print(f'going {direction}', position)
            while True:
                new_y, new_x = new_position(position=position, direction=direction)
                if position[0] < 0 or position[1] < 0:
                    with open('new_test_input.txt', 'w') as f:
                        f.writelines(new_test_input)
                    return
                try:
                    if raw_input[new_y][new_x] == '.' or raw_input[new_y][new_x] == '^':
                        temp_list = list(new_test_input[position[0]])
                        temp_list[position[1]] = 'X'
                        temp_str = ''.join(temp_list)
                        new_test_input[position[0]] = temp_str
                        with open('new_test_input.txt', 'w') as f:
                            f.writelines(new_test_input)
                        position = [new_y, new_x]
                    elif raw_input[new_y][new_x] == '#':
                        break
                except IndexError:
                    print(IndexError)
                    temp_list = list(new_test_input[position[0]])
                    temp_list[position[1]] = 'X'
                    temp_str = ''.join(temp_list)
                    new_test_input[position[0]] = temp_str
                    with open('new_test_input.txt', 'w') as f:
                        f.writelines(new_test_input)
                    return result


def second_star():
    result = 0
    print(f'{result=}')
    return result


def new_position(position: list [int, int], direction: str) -> list [int, int] | bool:
    directions = ([-1, 0], [0, 1], [1, 0], [0, -1])
    if direction == 'u':
        return [position[0]+directions[0][0], position[1]+directions[0][1]]
    elif direction == 'r':
        return [position[0]+directions[1][0], position[1]+directions[1][1]]
    elif direction == 'd':
        return [position[0]+directions[2][0], position[1]+directions[2][1]]
    elif direction == 'l':
        return [position[0]+directions[3][0], position[1]+directions[3][1]]

def find_asterix(grid: list[str]):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '^':
                print(f"^ in {y}, {x}")
                return [x, y]

if __name__ == '__main__':
    first_star()
    with open('new_test_input.txt', 'r') as f:
        new_test_input = f.readlines()
    result_1 = 0
    for i in new_test_input:
        result_1 += Counter(i)['X']
        # print(i, Counter(i)['X'])

    print(f'{result_1=}')
    second_star()
