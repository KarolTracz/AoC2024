git statuswith open('input_test.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [i.strip() for i in raw_data]


def first_star(data):
    result = 0
    print(f'first_star {result=}')


def second_star(data):
    result = 0
    print(f'first_star {result=}')


if __name__ == '__main__':
    first_star(data)
    second_star(data)
