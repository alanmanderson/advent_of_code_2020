INPUT_FILE = 'my_input.txt'

def get_input(filename):
    data = []
    with open(filename, 'r') as fp:
        for line in fp:
            data.append(int(line))
    return data

def get_two_sum_numbers(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i], data[j]


def get_three_sum_numbers(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            for k in range(j + 1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i], data[j], data[k]

data = get_input(INPUT_FILE)
#i, j = get_two_sum_numbers(data)
#print(i, j, i*j)

i, j, k = get_three_sum_numbers(data)
print(i, j, k, i * j * k)
