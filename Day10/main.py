with open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [i.strip() for i in raw_data]

def find_zero(height_map: [str]) -> [(int, int), (int, int)]:
    zeros = []

    for i, row in enumerate(height_map):
        for j, char in enumerate(row):
            if char == '0':
                zeros.append((i, j))
    return zeros

def find_neighbour(height_map:[str], position: (int, int)):
    pass

def fine_all_1_to_9(height_map, start_position:(int, int)):
    slope = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    find_neighbour(height_map, start_position)
    pass

def first_star(data):
    zeros = find_zero(height_map=data)
    for position in zeros:
        fine_all_1_to_9(height_map=data, start_position=position)
    print(zeros)

def second_star():
    pass


if __name__ == '__main__':
    first_star(data)
    second_star()
