import argparse

def read_input(filename):
    output = []
    with open(filename, 'r') as fp:
        for line in fp:
            output.append(int(line.strip()))
    return output

def differences(adapters):
    adapters.sort()
    adapters.insert(0,0)
    adapters.insert(len(adapters), max(adapters) + 3)
    diffs = {1:0, 2:0, 3:0}
    prev = None
    for i in adapters:
        if prev == None:
            prev = i
            continue
        diffs[i - prev] += 1
        prev = i
    return diffs

def count_combos():
    print(adapters)

def combo_helper(adapters):
    if len(adapters) == 2 and adapters[1] - adapters[0] <= 3:
        return 1
    if len(adapters) == 2 and adapters[1] - adapters[0] > 3:
        return 0
    else return 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('filename', type=str, default='my_input.txt')
    #parser.add_argument('int', type=int, default=0)
    args = parser.parse_args()
    adapters = read_input(args.filename)
    adapters.sort()
    diffs = differences(adapters)
    print(diffs)
    combos = count_combos()
