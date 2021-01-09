import re
import pprint

def get_input_lines():
    with open('day03\input.txt', 'r') as input_file:
        lines = [line.rstrip().replace('.', '0').replace('#', '1') for line in input_file]
        return lines


def count_trees(input_lines, slope_right, slope_down):
    lines = input_lines
    
    if slope_down > 1:
        lines = [line for index, line in enumerate(lines) if index % slope_down == 0]

    line_length = len(lines[0])
    trees_count = 0
    for index, line in enumerate(lines):
        horizontal_position = (slope_right * index) % line_length
        trees_count += int(line[horizontal_position])
    return trees_count

def main():
    lines = get_input_lines()
    print('Solution to first puzzle: ' + str(count_trees(lines, 3, 1)))

    count_slope_1_1 = (count_trees(lines, 1, 1))
    count_slope_3_1 = (count_trees(lines, 3, 1))
    count_slope_5_1 = (count_trees(lines, 5, 1))
    count_slope_7_1 = (count_trees(lines, 7, 1))
    count_slope_1_2 = (count_trees(lines, 1, 2))
    print('Solution to first puzzle: ' +
        str(count_slope_1_1 * count_slope_3_1 * count_slope_5_1 * count_slope_7_1 * count_slope_1_2))

if __name__ == '__main__':
    main()
