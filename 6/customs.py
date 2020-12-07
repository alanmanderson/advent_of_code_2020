INPUT_FILE = 'my_input.txt'

responses = []
with open(INPUT_FILE) as fp:
    group = []
    for line in fp:
        line = line.strip()
        if line == '':
            responses.append(group)
            group = []
            continue
        group.append(line)

affirmatives = []
total_all_yes = 0
for group in responses:
    yes = {}
    for person in group:
        for char in person:
            yes[char] = yes.get(char, 0) + 1
    for y in yes:
        if yes[y] == len(group):
            total_all_yes += 1
    affirmatives.append(len(yes))

print(total_all_yes)
print(len(responses), len(affirmatives))
print(responses[-1])
print(affirmatives)
print(sum(affirmatives))
