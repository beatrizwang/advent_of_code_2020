import re
import pprint


def get_numbers():
    with open('day1\input.txt', 'r') as input_file:
        numbers = [int(line.rstrip()) for line in input_file]
        return numbers

def find_pair_sum_2020(numbers):
    for number in numbers:
        for number_complement in numbers.copy():
            if (int(number_complement) + int(number) == 2020):
                print(number, number_complement)

def find_ternary_sum_2020(numbers):
    for number in numbers:
        for number_complement in numbers.copy():
            if (int(number_complement) + int(number) == 2020):
                print(number, number_complement)


def main():
    numbers = get_numbers()
    numbers.sort()
    min_number1, min_number2 = numbers[0], numbers[1]
    max_number1, max_number2 = numbers[-1], numbers[-2]
    maximum = 2020 - min_number1 - min_number2
    optional_numbers = [number for number in numbers if number <= maximum]
    print(optional_numbers)


if __name__ == '__main__':
    main()