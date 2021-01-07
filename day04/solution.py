import re
import pprint

expected_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
allowed_missing_fields = ['cid']
expected_fields_strict = [
    ('byr', 'byr:\d{4}'),
    ('iyr', 'iyr:\d{4}'),
    ('eyr', 'eyr:\d{4}'),
    ('hgt', 'hgt:\d+(cm|in)'),
    ('hcl', 'hcl:#[0-9abcdef]{6}'),
    ('ecl', 'ecl:(amb|blu|brn|gry|grn|hzl|oth)'),
    ('pid', 'pid:\d{9}\\b')
]

def get_passports():
    with open('day4\input.txt', 'r') as input_file:
        inputText = input_file.read()
        return (inputText.split('\n\n'))


def check_passport(passport):
    valid_passport = 0
    for field in expected_fields:
        # print (field)
        # print(re.search(field + ':', passport))
        if not re.search(field + ':', passport) and field not in allowed_missing_fields:
            return False
    return True


def check_passport_strict(passport):
    valid_passport = 0
    for field in expected_fields_strict:
        match = re.search(field[1], passport)
        # print(field[0])
        if match and field[0] == 'byr':
            year = int(match.group()[-4:])
            if year < 1920 or year > 2002:
                return False
        if match and field[0] == 'iyr':
            year = int(match.group()[-4:])
            if year < 2010 or year > 2020:
                return False
        if match and field[0] == 'eyr':
            year = int(match.group()[-4:])
            if year < 2020 or year > 2030:
                return False
        if match and field[0] == 'hgt':
            number_match = re.search('\d+', match.group())
            
            if number_match and 'in' in match.group():
                height = int(number_match.group())
                if height < 59 or height > 76:
                    return False
            if number_match and 'cm' in match.group():
                height = int(number_match.group())
                if height < 150 or height > 193:
                    return False
            if 'cm' not in match.group() and 'in' not in match.group():
                return False
        if not match and field[0] not in allowed_missing_fields:
            return False
    return True

def main():
    passports = get_passports()
    count = 0
    for passport in passports:
        if check_passport_strict(passport):
            count += 1
    print(count)

#     passport='''
# byr:2000
# ecl:hzl
# cid:178 hcl:#a97842 iyr:2010 hgt:60in eyr:2021 pid:000143498
# '''
#     print(check_passport_strict(passport))

if __name__ == '__main__':
    main()
