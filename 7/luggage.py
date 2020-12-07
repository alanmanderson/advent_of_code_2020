INPUT_FILE = 'my_input.txt'

def get_rules(filename):
    with open(filename, 'r') as fp:
        rules = []
        for line in fp:
            rules.append(parse_rule(line.strip()))
    return rules

def parse_rule(txt_rule):
    print(txt_rule)
    bag, contains = txt_rule.split(' bags contain ')
    contains = contains.split(',')
    bags_contained = []
    for contain in contains:
        contain = contain.replace('.', '').strip()
        number, contains_color = contain.split(' ', 1)
        if number == 'no':
            return bag, []
        contains_color, _ = contains_color.rsplit(' ', 1)
        bags_contained.append((int(number), contains_color))
    return bag, bags_contained

def get_contains_tree(rules):
    tree = {}
    for bag, contains in rules:
        if bag not in tree:
            tree[bag] = []
        for _, color in contains:
            if color not in tree:
                tree[color] = []
            tree[color].append(bag)
    return tree

def traverse_contains_tree(tree, color):
    queue = [color]
    seen = {}
    while len(queue) > 0:
        col = queue.pop(0)
        print(col, len(queue))
        seen[col] = True
        for bag in tree[col]:
            if bag in seen:
                continue
            queue.append(bag)
    return seen

def get_tree(rules):
    tree = {}
    for bag, contains in rules:
        tree[bag] = contains
    return tree

def traverse_tree(tree, color):
    bags = tree[color]
    total_count = 1
    for cnt, bag in bags:
        sub_count = traverse_tree(tree, bag)
        print(color, bag, cnt, sub_count)
        total_count += cnt * sub_count
    return total_count

# part 1:
rules = get_rules(INPUT_FILE)
tree = get_contains_tree(rules)
seen = traverse_contains_tree(tree, 'shiny gold')
print(seen)
print(len(seen))

# part 2:
tree = get_tree(rules)
cnt = traverse_tree(tree, 'shiny gold')
print(cnt)
