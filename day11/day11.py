import re
import pprint
import copy

def get_seats():
    seats = []
    with open('day11\input.txt', 'r') as input_file:
        for line in input_file:
            seats.append(list(line.rstrip()))
        return seats

def empty_seat_becomes_occupied(seats, row, column):
    rows = []
    if row == 0:
        rows = [row, row + 1]
    elif row == len(seats) - 1:
        rows = [row - 1, row]
    else:
        rows = [row - 1, row, row + 1]

    columns = []
    if column == 0:
        columns = [column, column + 1]
    elif column == len(seats[0]) - 1:
        columns = [column - 1, column]
    else:
        columns = [column - 1, column, column + 1]
        
    for r in rows:
        for c in columns:
            if seats[r][c] == '#':
                return False
    return True

def occupied_seat_becomes_empty(seats, row, column):
    count_occupied = 0

    rows = []
    if row == 0:
        rows = [row, row + 1]
    elif row == len(seats) - 1:
        rows = [row - 1, row]
    else:
        rows = [row - 1, row, row + 1]

    columns = []
    if column == 0:
        columns = [column, column + 1]
    elif column == len(seats[0]) - 1:
        columns = [column - 1, column]
    else:
        columns = [column - 1, column, column + 1]
    
    for r in rows:
        for c in columns:
            if seats[r][c] == '#':
                count_occupied += 1

    count_occupied -= 1
    return count_occupied >= 4

def apply_rules_adjacent(seats):
    indices_convert_empty = []
    indices_convert_occupied = []
    for row_index, row_lines in enumerate(seats):
        for column_index, seat in enumerate(row_lines):
            if seat == 'L' and empty_seat_becomes_occupied(seats, row_index, column_index):
                indices_convert_occupied.append((row_index, column_index))
            if seat == '#' and occupied_seat_becomes_empty(seats, row_index, column_index):
                indices_convert_empty.append((row_index, column_index))
    for indices in indices_convert_empty:
        seats[indices[0]][indices[1]] = 'L'
    for indices in indices_convert_occupied:
        seats[indices[0]][indices[1]] = '#'
    return seats

def get_answer_1():
    seats = get_seats()
    seats_copy = copy.deepcopy(seats)
    modified_seats = apply_rules_adjacent(seats_copy)
    while (seats != modified_seats):
        seats = copy.deepcopy(modified_seats)
        seats_copy = copy.deepcopy(seats)
        modified_seats = apply_rules_adjacent(seats_copy)

    count_occupied = 0
    for row_seat in modified_seats:
        for seat in row_seat:
            if seat == '#':
                count_occupied += 1
    return count_occupied

def empty_seat_becomes_occupied_visible_mode(seats, row, column):
    if get_first_seat_left(seats, row, column) == '#':
        return False
    if get_first_seat_right(seats, row, column) == '#':
        return False
    if get_first_seat_up(seats, row, column) == '#':
        return False
    if get_first_seat_down(seats, row, column) == '#':
        return False
    if get_first_seat_up_left(seats, row, column) == '#':
        return False
    if get_first_seat_up_right(seats, row, column) == '#':
        return False
    if get_first_seat_down_left(seats, row, column) == '#':
        return False
    if get_first_seat_down_right(seats, row, column) == '#':
        return False
    return True

def occupied_seat_becomes_empty_visible_mode(seats, row, column):
    count_occupied = 0

    if get_first_seat_left(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_right(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_up(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_down(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_up_left(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_up_right(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_down_left(seats, row, column) == '#':
        count_occupied += 1
    if get_first_seat_down_right(seats, row, column) == '#':
        count_occupied += 1

    return count_occupied >= 5

def get_first_seat_left(seats, row, column):
    for index in range(column):
        seat_letter = seats[row][column - index - 1]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_right(seats, row, column):
    for index in range(len(seats[0]) - column - 1):
        seat_letter = seats[row][column + index + 1]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_up(seats, row, column):
    for index in range(row):
        seat_letter = seats[row - index - 1][column]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_down(seats, row, column):
    for index in range(len(seats) - row - 1):
        seat_letter = seats[row + index + 1][column]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_up_left(seats, row, column):
    max_distance = min(row, column)
    for index in range(max_distance):
        seat_letter = seats[row - index - 1][column - index - 1]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_up_right(seats, row, column):
    max_distance = min(row, len(seats[0]) - column - 1)
    for index in range(max_distance):
        seat_letter = seats[row - index - 1][column + index + 1]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_down_left(seats, row, column):
    max_distance = min(len(seats) - row - 1, column)
    for index in range(max_distance):
        seat_letter = seats[row + index + 1][column - index - 1]
        if seat_letter != '.':
            return seat_letter
    return None

def get_first_seat_down_right(seats, row, column):
    max_distance = min(len(seats) - row - 1, len(seats[0]) - column - 1)
    for index in range(max_distance):
        seat_letter = seats[row + index + 1][column + index + 1]
        if seat_letter != '.':
            return seat_letter
    return None

def apply_rules_visible(seats):
    indices_convert_empty = []
    indices_convert_occupied = []
    for row_index, row_lines in enumerate(seats):
        for column_index, seat in enumerate(row_lines):
            if seat == 'L' and empty_seat_becomes_occupied_visible_mode(seats, row_index, column_index):
                indices_convert_occupied.append((row_index, column_index))
            if seat == '#' and occupied_seat_becomes_empty_visible_mode(seats, row_index, column_index):
                indices_convert_empty.append((row_index, column_index))
    for indices in indices_convert_empty:
        seats[indices[0]][indices[1]] = 'L'
    for indices in indices_convert_occupied:
        seats[indices[0]][indices[1]] = '#'
    return seats

def get_answer_2():
    seats = get_seats()
    seats_copy = copy.deepcopy(seats)
    modified_seats = apply_rules_visible(seats_copy)
    while (seats != modified_seats):
        seats = copy.deepcopy(modified_seats)
        seats_copy = copy.deepcopy(seats)
        modified_seats = apply_rules_visible(seats_copy)

    count_occupied = 0
    for row_seat in modified_seats:
        for seat in row_seat:
            if seat == '#':
                count_occupied += 1
    return count_occupied


def main():
    print(get_answer_1())
    print(get_answer_2())

if __name__ == '__main__':
    main()