def import_data():
    with open('input.txt', 'r') as f:
    # with open('test_input.txt', 'r') as f:
        equazion = {}
        raw_input = f.readlines()
        lines = [i.split(':') for i in raw_input]
        print(lines)
        for line in lines:
            equazion[line[0]] = [int(i) for i in line[1].split()]
    print(f'{equazion=}')
    return equazion


def options_generator(lenght: int) -> [str]:
    initial_value = '+' * int(lenght-1)
    count = 0
    results = []
    while True:
        count += 1
        # print(f'{len(results)=}, {count=}, {results=}')
        if initial_value not in results:
            results.append(initial_value)
        else:
            for i, char in enumerate(initial_value):
                if len(results) == 3 ** (lenght-1):
                    return results
                elif char == '+':
                    new = list(initial_value)
                    new[i] = '|'
                    initial_value = ''.join(new)
                    break
                elif char == '|':
                    new = list(initial_value)
                    new[i] = '*'
                    initial_value = ''.join(new)
                    break
                elif char == '*':
                    new = list(initial_value)
                    new[i+1] = '*'
                    new[i] = '+'
                    initial_value = ''.join(new)


def main():
    result = 0
    data = import_data()
    for k, v in data.items():
        print(f'finding {k=} for {v=}')
        for option in generate_all_combinations(len(v)-1):
            cur_val = 0
            for i, sign in enumerate(option):
                if i == 0 and sign == '+':
                    cur_val = (v[i] + v[i+1])
                elif sign == '+':
                    cur_val += v[i+1]
                elif i == 0 and sign == '*':
                    cur_val = (v[i] * v[i+1])
                elif sign == '*':
                    cur_val = cur_val * v[i+1]
                elif i == 0 and sign == '|':
                    cur_val = int(str(v[i]) + str(v[i+1]))
                elif sign == '|':
                    cur_val = int(str(cur_val) + str(v[i+1]))
            if int(k) == cur_val:
                print(f'{int(k)==cur_val=} {option=}')
                result += int(k)
                break
    print(f'{result=}')

def generate_all_combinations(length):
    symbols = ['+', '*', '|']
    total_numbers = 3 ** length
    combinations = []

    for i in range(total_numbers):
        combination = decimal_to_custom_ternary(i)
        # Pad with '+' to ensure fixed length
        combination = combination.rjust(length, '+')
        combinations.append(combination)

    return combinations

def decimal_to_custom_ternary(n):
    if n == 0:
        return '+'

    symbols = ['+', '*', '|']
    result = ''

    while n > 0:
        remainder = n % 3
        result = symbols[remainder] + result
        n //= 3

    return result


if __name__ == '__main__':
    main()
