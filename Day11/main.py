from typing import List

# with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    puzzle_input = f.readline().split()

def blink(data: List[str]) -> List[str]:
    result = []

    for i in data:
        if len(i) % 2 == 0:
            result.append(str(int(i[:len(i)//2])))
            result.append(str(int(i[len(i)//2:])))
        elif i == '0':
            result.append('1')
        else:
            result.append(str(int(i)*2024))

    return result


def first_star(data):
    result = 0
    print(f'{data=}')

    number_of_blinks = 25
    blint_data = blink(data)
    for _ in range(number_of_blinks-1):
        new_blink_data = blink(blint_data)
        blint_data = new_blink_data
    result += len(blint_data)
    print(f'first_star {result=}')


def second_star(data):
    result = 0
    print(f'first_star {result=}')


if __name__ == '__main__':
    first_star(puzzle_input)
    second_star(puzzle_input)
