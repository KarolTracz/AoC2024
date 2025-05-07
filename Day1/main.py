from collections import Counter

def first_star():
    with open('input.txt', 'r') as f:
    # with open('input_test.txt', 'r') as f:
        raw_input = f.readlines()

    l_list = []
    r_list = []
    for i in raw_input:
        i_split = i.split()
        l_list.append(int(i_split[0]))
        r_list.append(int(i_split[1]))
    l_list.sort()
    r_list.sort()

    result_first_star = 0
    for i in range(len(l_list)):
        result_first_star += (abs(l_list[i] - r_list[i]))
    print(f'{result_first_star=}')
    return result_first_star


def second_star():
    with open('input.txt', 'r') as f:
    # with open('input_test.txt', 'r') as f:
        raw_input = f.readlines()

    l_list = []
    r_list = []
    for i in raw_input:
        i_split = i.split()
        l_list.append(i_split[0])
        r_list.append(i_split[1])
    r_count = Counter(r_list)

    result_second_star = 0
    for i in l_list:
        if i in r_count.keys():
            result_second_star += int(i) * int(r_count[i])

    print(f'{result_second_star=}')
    return result_second_star


if __name__ == '__main__':
    first_star()
    second_star()
