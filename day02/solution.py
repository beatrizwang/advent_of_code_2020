import re
import pprint

def get_lines():
    with open('day02\input.txt', 'r') as input_file:
        lines = [line.rstrip().split(':') for line in input_file]
        return lines


def count_valid_passwords_by_letter_count(lines):
    count_valid_pass = 0;
    for line in lines:
        required_letter = line[0][-1]
        min_rep, max_rep = re.findall('\d+', line[0])
        password = line[1]
        count_required_letters = password.count(required_letter)
        if count_required_letters <= int(max_rep) and count_required_letters >= int(min_rep):
            count_valid_pass += 1
    return count_valid_pass

def count_valid_passwords_by_letter_position(lines):
    count_valid_pass = 0;
    for line in lines:
        required_letter = line[0][-1]
        first_position, second_position = re.findall('\d+',line[0])
        password = line[1]
        first_letter = password.strip()[int(first_position) - 1]
        second_letter = password.strip()[int(second_position) - 1]
        if ((first_letter == required_letter and second_letter != required_letter) or
            (first_letter != required_letter and second_letter == required_letter)):
            count_valid_pass += 1
    return count_valid_pass

def main():
    lines = get_lines()
    print('Solution to first puzzle: ' + str(count_valid_passwords_by_letter_count(lines)))
    print('Solution to second puzzle: ' + str(count_valid_passwords_by_letter_position(lines)))

if __name__ == '__main__':
    main()
