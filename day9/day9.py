import re
import pprint
import itertools

def get_numbers():
    with open('day9\input.txt', 'r') as input_file:
        inputText = input_file.read()
        return [int(line) for line in inputText.split('\n')]

def is_sum_of_previous_numbers(numbers, index, size_of_group):
    my_group = numbers[index - size_of_group: index]
    for combination in list(itertools.combinations(my_group, 2)):
        if numbers[index] == combination[0] + combination[1]:
            return True
    return False

def find_first_number_not_sum(numbers, size_of_group):
    for index, number in enumerate(numbers):
        if (index < size_of_group):
            pass
        elif not is_sum_of_previous_numbers(numbers, index, size_of_group):
            return number

def sum_contiguous_numbers(numbers, index, size_of_group):
    return sum(numbers[index: index + size_of_group])

def find_contiguous_numbers_sum(numbers, sum):
    max_index = numbers.index(sum)
    for index in range(max_index):
        for size in range(max_index - index):
            if sum_contiguous_numbers(numbers, index, size) == sum:
                return index, size

def main():
    numbers = get_numbers()
    # print(find_first_number_not_sum(numbers, 25))
    # print(is_sum_of_previous_numbers(numbers, 174, 25))
    index, size = (find_contiguous_numbers_sum(numbers, 530627549))
    group = numbers[index: index + size]
    pprint.pprint(group)
    print(max(group) + min(group))


if __name__ == '__main__':
    main()