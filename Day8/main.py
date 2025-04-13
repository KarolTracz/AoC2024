from itertools import combinations

# with open('test_data.txt', 'r') as f:
# with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [i.strip() for i in raw_data]


def first_star(map):
    print(f'{'-'* 10} first_star {'-'* 10}')
    antennas = {}
    antinodes = []

    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != '.':
                if char in antennas:
                    tmp = antennas[char]
                    tmp.append([i, j])
                    antennas[char] = tmp
                else:
                    antennas[str(char)] = [[i, j]]

    print(f'{antennas=}')
    for k, v in antennas.items():
        for comb in combinations(v, 2):
            x, y = (comb[0][0] - comb[1][0]), (comb[0][1] - comb[1][1])
            x1, y1 = comb[0][0] + x, comb[0][1] + y
            x2, y2 = comb[1][0] - x, comb[1][1] - y
            try:
                if len(map) <= x1 or x1 < 0 or len(row) <= y1 or y1 < 0:
                    pass
                else:
                    antinodes.append((x1, y1))

                if len(map) <= x2 or x2 < 0 or len(row) <= y2 or y2 < 0:
                    pass
                else:
                    antinodes.append((x2, y2))
            except IndexError:
                pass

    return len(set(antinodes))


if __name__ == '__main__':
    print(first_star(data))
