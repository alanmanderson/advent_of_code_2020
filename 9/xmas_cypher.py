INPUT_FILE = 'my_input.txt'

def read_cypher(filename):
    ints = []
    with open(filename, 'r') as fp:
        for line in fp:
            ints.append(int(line.strip()))
    return ints

def find_error(ints, preamble):
    for i in range(preamble, len(ints)):
        pair = None
        for x in range(i - preamble, i):
            for y in range(x, i):
                if x == y:
                    continue
                if ints[x] + ints[y] == ints[i]:
                    pair = (x, y)
        if pair == None:
            return ints[i]

ints = read_cypher(INPUT_FILE)
target_sum = find_error(ints, 25)
#ints = read_cypher('sample_input.txt')
#target_sum = find_error(ints, 5)

def find_ints_sum(target_sum):
    start = 0
    end = 1
    while True:
        cur_sum = sum(ints[start : end])
        if cur_sum == target_sum:
            return ints[start : end]
        elif cur_sum < target_sum:
            end +=1
        elif cur_sum > target_sum:
            start += 1
    return None

def brute_find_ints_sum(start_idx, end_idx, target_sum):
    print(start_idx, end_idx)
    if start_idx >= end_idx:
        return None
    if start_idx < 0:
        return None
    cur_sum = sum(ints[start_idx:end_idx])
    if cur_sum == target_sum:
        return ints[start_idx:end_idx]
    next_try = find_ints_sum(start_idx, end_idx - 1, target_sum)
    if next_try != None:
        return next_try
    return find_ints_sum(start_idx + 1, end_idx, target_sum)

cypher = find_ints_sum(target_sum)
#cypher = find_ints_sum(0, len(ints), target_sum)
print(cypher)
print(min(cypher) + max(cypher))
print(cypher[0] + cypher[-1])
