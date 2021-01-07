import re
import pprint

def get_lines():
    with open('day3\input.txt', 'r') as input_file:
        lines = [line.rstrip().replace('.', '0').replace('#', '1') for line in input_file]
        return lines


def count_trees(right_positions, down_positions):
    lines = get_lines()
    if down_positions > 1:
        lines = [line for index, line in enumerate(lines) if index % down_positions == 0]

    index = 0
    count = 0
    for line in lines:
        position = (right_positions * index) % 31
        count += int(line[position])
        index += 1
    return count

def main():
    result1 = (count_trees(1, 1))
    result2 = (count_trees(3, 1))
    result3 = (count_trees(5, 1))
    result4 = (count_trees(7, 1))
    result5 = (count_trees(1, 2))
    print(result1 * result2 * result3 * result4 * result5)

if __name__ == '__main__':
    main()
