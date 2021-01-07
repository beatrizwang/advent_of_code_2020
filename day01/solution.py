import re
import pprint


def get_numbers():
    with open('day01\input.txt', 'r') as input_file:
        numbers = [int(line.rstrip()) for line in input_file]
        return numbers

def find_pair_sum_target(numbers, target):
    for first_term in numbers:
        for second_term in numbers.copy():
            if (int(second_term) + int(first_term) == target):
                return first_term, second_term

def find_ternary_sum_target(numbers, target):
    for first_term in numbers:
        for second_term in numbers.copy():
            for third_term in numbers.copy():
                if (int(first_term) + int(second_term) + int(third_term) == target):
                    return first_term, second_term, third_term


def main():
    numbers = get_numbers()

    #First puzzle
    number1, number2 = find_pair_sum_target(numbers, 2020)
    print('Solution to first puzzle: ' + str(number1 * number2))

    #Second puzzle
    numbers.sort()
    min_number1, min_number2 = numbers[0], numbers[1]
    max_value_for_puzzle_2 = 2020 - min_number1 - min_number2
    feasible_numbers = [number for number in numbers if number <= max_value_for_puzzle_2]
    number1, number2, number3 = find_ternary_sum_target(feasible_numbers, 2020)
    print('Solution to second puzzle: ' + str(number1 * number2 * number3))

if __name__ == '__main__':
    main()