# with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = f.readline()

sum_data = sum([int(i) for i in data])

def disk_2_space_and_files(data_map: str) -> str:
    result = {'spaces': [], 'files': []}
    file_id = 0
    for i, data in enumerate(data_map):
        if i % 2 == 1:
            # print("spaces")
            result['spaces'].append(int(data))
        else:
            result['files'].append((file_id, int(data)))
            # print(file_id)
            file_id += 1
    return result


def s_d2dict(spaces_files: dict) -> dict:
    spaces = spaces_files['spaces']
    files = spaces_files['files']
    result_dict = {}
    id_count = 0
    while True:
        print('if id_count >= sum_data', id_count, sum_data)
        if id_count >= sum_data:
            break
        try:
            for i in range(len(files)):
                for _ in range(files[i][1]):
                    result_dict[id_count] = files[i][0]
                    id_count += 1
                for _ in range(spaces[i]):
                    result_dict[id_count] = '.'
                    id_count += 1
        except IndexError:
            pass
    print(result_dict)
    return result_dict


def first_star(disk):
    sumcheck = 0
    final_disk = disk_data2string(disk)
    print(final_disk)
    for k, v in (final_disk.items()):
        print(k)
        if v != '.':
            sumcheck += k * v
    print(f'{sumcheck=}')



def disk_data2string(disk: dict) -> str:
    data = disk_2_space_and_files(disk)
    dict = s_d2dict(data)

    final_disk = dict.copy()
    for k, v in dict.items():
        print(k)
        if v == '.':
            for i in range(len(final_disk) - 1, -1, -1):
                if i > k:
                    break
                if isinstance(final_disk[i], int):
                    final_disk[i], final_disk[k] = final_disk[k], final_disk[i]
                    break


    return final_disk

def second_star(disk):

    result = 0
    return result


if __name__ == '__main__':
    print(data)
    first_star(data)
    second_star(data)
