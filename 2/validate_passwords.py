INPUT_FILE = 'my_input.txt'

def read_file(filename):
    with open(filename, 'r') as fp:
        data = []
        for line in fp:
            data.append(line.strip().split(': '))
    return data

def old_valid_passwords(data):
    valid_passwords = []
    for str_policy, password in data:
        policy = parse_policy(str_policy)
        letter_count = 0
        for i in password:
            if i == policy.letter:
                letter_count+=1
        if letter_count >= policy.min_letter and letter_count <= policy.max_letter:
            valid_passwords.append(password)
    return valid_passwords

def new_valid_passwords(data):
    valid_passwords = []
    for str_policy, password in data:
        policy = parse_policy(str_policy)
        if xor(password, policy.min_letter - 1, policy.max_letter - 1, policy.letter):
            valid_passwords.append(password)
    return valid_passwords

def xor(password, idx1, idx2, letter):
    return (password[idx1] == letter) != (password[idx2] == letter)

class Policy:
    def __init__(self, min_letter, max_letter, letter):
        self.min_letter = min_letter
        self.max_letter = max_letter
        self.letter = letter

def parse_policy(str_policy):
    parts = str_policy.split(' ')
    counts = parts[0].split('-')
    return Policy(int(counts[0]), int(counts[1]), parts[1])

data = read_file(INPUT_FILE)
pws = new_valid_passwords(data)
print(pws)
print(len(pws))
