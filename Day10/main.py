from typing import List, Tuple

with open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [i.strip() for i in raw_data]


def find_zero(height_map: [str]) -> List[Tuple[int, int]]:
    zeros = []

    for i, row in enumerate(height_map):
        for j, char in enumerate(row):
            if char == '0':
                zeros.append((i, j))
    return zeros


def find_neighbour(height_map:[str], position: (int, int), seeking_value: int) -> List[Tuple[True, Tuple[int]]]:
    result = []

    neighbours = ((-1, 0), (0, -1), (1, 0), (0, 1))
    for dx, dy in neighbours:
        x, y = position[0] + dx, position[1] + dy
        if x < 0 or y < 0:
            continue
        try:
            val = int(height_map[x][y])
        except IndexError:
            continue
        if val == seeking_value:
            result.append((True, (x, y)))
        else:
            result.append((False, (x, y)))

    return result


def find_all_1_to_9(height_map, start_position: Tuple[int]):
    score = 0
    slope = (2, 3, 4, 5, 6, 7, 8, 9)
    paths = []

    neighbours = find_neighbour(height_map=height_map, position=start_position, seeking_value=1)
    for neighbour in neighbours:
        if neighbour[0]:
            paths.append((1, neighbour[1]))
        else:
            pass

    for path in paths:
        for i in slope:
            if (path[0] + 1) == i:
                start_position = path[1]
            else:
                continue
            neighbours = find_neighbour(height_map=height_map, position=start_position, seeking_value=i)
            for neighbour in neighbours:
                if neighbour[0] == True:
                    paths.append((i, neighbour[1]))
                else:
                    pass

    for path in paths:
        if path[0] == 9:
            score += 1
    return score


def first_star(data):
    result = 0
    zeros = find_zero(height_map=data)
    for position in zeros:
        result += find_all_1_to_9(height_map=data, start_position=position)
    print(f'first_star {result=}')


def second_star():
    pass


if __name__ == '__main__':
    first_star(data)
    second_star()
