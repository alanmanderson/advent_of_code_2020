import re

INPUT_FILE = 'my_input.txt'
REQUIRED_FIELDS = [ 'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt' ]

def get_passports(filename):
    with open(filename, 'r') as fp:
        passports = []
        current_passport = ''
        for line in fp:
            line = line.strip()
            if line == '':
                passports.append(current_passport.strip())
                current_passport = ''
            else:
                current_passport +=  ' ' + line
    return parse_passports(passports)

def parse_passports(passports):
    p = []
    for i in passports:
        kvs = i.split(" ")
        passport = {}
        for kv in kvs:
            key, value = kv.split(':')
            passport[key] = value
        p.append(passport)
    return p

def valid_passports(passports):
    valids = []
    for p in passports:
        required_fields = 0
        for field in REQUIRED_FIELDS:
            if field in p and validate(field, p[field]):
                required_fields += 1
        if required_fields == len(REQUIRED_FIELDS):
            valids.append(p)
    return valids

def validate(field, value):
    if field == 'byr':
        value = int(value)
        return value >= 1920 and value <= 2002
    if field == 'iyr':
        value = int(value)
        return value >= 2010 and value <= 2020
    if field == 'eyr':
        value = int(value)
        return value >= 2020 and value <= 2030
    if field == 'hgt':
        if value.endswith('cm'):
            value = int(value[:-2])
            return value >= 150 and value <= 193
        elif value.endswith('in'):
            value = int(value[:-2])
            return value >= 59 and value <= 76
        return False
    if field == 'hcl':
        return re.fullmatch(r'#[a-f0-9]{6}', value) is not None
    if field == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if field == 'pid':
        return re.fullmatch(r'[0-9]{9}', value) is not None
    return True

passports = get_passports(INPUT_FILE)
passports = valid_passports(passports)
print (len(passports))
