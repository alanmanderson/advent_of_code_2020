import argparse

def read_input(filename):
    output = []
    with open(filename, 'r') as fp:
        for line in fp:
            output.append(line.strip())

def solve(in_arr):
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('filename', type=str, default='my_input.txt')
    parser.add_argument('int', type=int, default=0)
    args = parser.parse_args()
    in_arr = read_input(args.filename)
    sln = solve(in_arr)
    print(sln)
