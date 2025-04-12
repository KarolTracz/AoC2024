from itertools import combinations

# with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [i.strip() for i in raw_data]

# with open('test_data.txt', 'r') as f:
#     raw_data = f.readlines()
#     test_data = [i.strip() for i in raw_data]



def first_star(map):
    print(f'{'-'* 10} first_star {'-'* 10}')
    result = 0
    antennas = {}

    for line, row in enumerate(map):
        row = row
        for j, char in enumerate(row):
            if char != '.':
                if char in antennas:
                    tmp = antennas[char]
                    tmp.append([line, j])
                    antennas[char] = tmp
                else:
                    antennas[str(char)] = [[line, j]]
    print(f'{antennas=}')
    map_copy = map.copy()
    for k, v in antennas.items():
        for comb in combinations(v, 2):
            x, y = (comb[0][0] - comb[1][0]), (comb[0][1] - comb[1][1])
            try:
                if (comb[0][0] + x) < 0:
                    pass
                else:
                    tmp_list = list(map_copy[comb[0][0] + x])
                    if tmp_list[comb[0][1] + y] != '#':
                        if tmp_list[comb[0][1] + y] == '.':
                            tmp_list[comb[0][1] + y] = '#'
                        result += 1
                    map_copy[comb[0][0] + x] = ''.join(tmp_list)

                if (comb[1][0] - x) < 0:
                    pass
                else:
                    tmp_list = list(map_copy[comb[1][0] - x])
                    if tmp_list[comb[1][1] - y] != '#':
                        if tmp_list[comb[1][1] - y] == '.':
                            tmp_list[comb[1][1] - y] = '#'
                        result += 1
                    map_copy[comb[1][0] - x] = ''.join(tmp_list)
            except IndexError:
                pass

    print(f'{result=}')
    print('COMPARE')
    # for i, line in enumerate(map_copy):
    #     print(map[i], line, test_data[i], line == test_data[i])

def second_star(data):
    print(f'{'-'* 10} second_star {'-'* 10}')


if __name__ == '__main__':
    first_star(data)
    print(f'{'-'* 10} * {'-'* 10}')
    second_star(data)
