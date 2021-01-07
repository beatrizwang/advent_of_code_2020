import re
import pprint

def get_lines():
    with open('day2\input.txt', 'r') as input_file:
        lines = [line.rstrip().split(':') for line in input_file]
        return lines


def count_valid_passwords():
    lines = get_lines()
    count = 0;
    for line in lines:
        letter = line[0][-1]
        minimum, maximum = re.findall('\d+',line[0])
        count_letters = line[1].count(letter)
        if count_letters <= int(maximum) and count_letters >= int(minimum):
            count += 1
    print(count)

def count_valid_passwords2():
    lines = get_lines()
    count = 0;
    for line in lines:
        letter = line[0][-1]
        position1, position2 = re.findall('\d+',line[0])
        first_letter = line[1].strip()[int(position1) - 1]
        second_letter = line[1].strip()[int(position2) - 1]
        if (first_letter == letter and second_letter != letter) or (first_letter != letter and second_letter == letter):
            count += 1
    print(count)

def main():
    count_valid_passwords2()

if __name__ == '__main__':
    main()