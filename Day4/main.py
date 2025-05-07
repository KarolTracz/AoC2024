def main():
    board = import_data()
    possitions_of_x = find_all_X(board)
    result = 0
    for i in possitions_of_x:
        m_with_dir = find_m(i, board)
        for i in m_with_dir:
            a_s = find_a_s(board=board, position=[i[0], i[1]], direction=i[2])
            if a_s == []:
                pass
            else:
                result += 1
    print(result)

def import_data():
    # with open('input_test.txt', 'r') as f:
    with open('input.txt', 'r') as f:
        raw_input = f.readlines()
    print(f'import_data() return {[i.strip() for i in raw_input]=}')
    return [i.strip() for i in raw_input]

def find_all_X(board: list[str]):
    possitions_of_x = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'X':
                possitions_of_x.append([i,j])
    print(f'{possitions_of_x=}')
    return possitions_of_x

def find_m(position: [int, int], board: list[str]):
    all_m = []
    directions = (
        [0, -1],
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1]
    )
    if board[position[0]][position[1]] == 'X':
        for direction in directions:
            new_position = [position[0]+direction[0], position[1]+direction[1]]
            try:
                if board[new_position[0]][new_position[1]] == 'M' and new_position[0] > 0:
                    all_m.append([new_position[0], new_position[1], direction])
            except IndexError:
                pass
    return all_m

def find_a_s(position: [int, int], direction:[int, int], board: list[str]):
    all_a_s = []
    if board[position[0]][position[1]] == 'M':
        new_position = [position[0] + direction[0], position[1] + direction[1]]
        try:
            if board[new_position[0]][new_position[1]] == 'A':
                new_position = [position[0] + 2*direction[0], position[1] + 2*direction[1]]
                if board[new_position[0]][new_position[1]] == 'S':
                    all_a_s.append(new_position[0])
                    all_a_s.append(new_position[1])
                    all_a_s.append(direction)
        except IndexError:
            pass
    return all_a_s

if __name__ == '__main__':
    main()
