with open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
def first_star(data):
    print(f'{'-'* 10} first_star {'-'* 10}')
    antennas = {}
    for i, row in enumerate(data):
        row = row.strip()
        for j, char in enumerate(row):
            if char != '.':
                if char in antennas:
                    tmp = antennas[char]
                    tmp.append([i, j])
                    antennas[char] = tmp
                else:
                    antennas[str(char)] = [[i, j]]
        print(i, antennas)


def second_star(data):
    print(f'{'-'* 10} second_star {'-'* 10}')


if __name__ == '__main__':
    print(f'{raw_data=}')
    first_star(raw_data)
    print(f'{'-'* 10} * {'-'* 10}')
    print("""......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.""")
    second_star(raw_data)
