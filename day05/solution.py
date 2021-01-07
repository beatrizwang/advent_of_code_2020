import re
import pprint

def get_binary_seats():
    seats = []
    with open('day5\input.txt', 'r') as input_file:
        for line in input_file:
            seats.append(get_seat_from_line(line))
        return seats

def get_seat_from_line(line):
    line = line.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return (line[0:7], line[7:])

def get_numeric_seats():
    binary_seats = get_binary_seats()
    return [(int(seat[0], 2), int(seat[1], 2)) for seat in binary_seats]

def main():
    seats = get_numeric_seats()
    # ids = [seat[0]* 8 + seat[1] for seat in seats]
    # print(max(ids))

    free_seats = []
    occupied_seats = []
    for row in range(0,127):
        for column in range(0,7):
            if (row, column) in seats:
                occupied_seats.append((row, column, row*8+column))
            else:
                free_seats.append((row, column, row*8+column))

    occupied_seats_ids = [seat[2] for seat in occupied_seats]
    for seat in free_seats:
        if (seat[2] - 1) in occupied_seats_ids and (seat[2] + 1) in occupied_seats_ids:
            print(seat)

if __name__ == '__main__':
    main()