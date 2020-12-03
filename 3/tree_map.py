INPUT_FILE = 'my_input.txt'
TREE = '#'
EMPTY = '.'

def get_map(filename):
    forest = []
    with open(filename, 'r') as fp:
        for line in fp:
            forest.append(line)
    return forest

def count_tree_intersects(forest, rise, run):
    location = [0,0]
    tree_count = 0
    section_width = len(forest[0]) - 1
    while location[1] + rise < len(forest):
        location[0] += run
        location[0] %= section_width
        location[1] += rise
        if forest[location[1]][location[0]] == TREE:
            tree_count += 1
            print(location, len(forest), section_width, 'X')
        else: print(location, len(forest), section_width, '.')
    return tree_count

forest = get_map(INPUT_FILE)
#tree_count = count_tree_intersects(forest, 1, 3)
#print(tree_count)

slopes = [ [1,1], [1,3], [1, 5], [1,7], [2,1] ]

tree_counts = []
for slope in slopes:
    tree_counts.append(count_tree_intersects(forest, slope[0], slope[1]))

product = 1
for tree_count in tree_counts:
    product *= tree_count

print(tree_counts, product)
