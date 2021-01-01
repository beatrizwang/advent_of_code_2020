import re
import pprint
import math

def get_input():
    with open('day13\input.txt', 'r') as input_file:
        earliest_timestamp = int(input_file.readline().strip())
        bus_lines = [int(line) for line in re.findall('\d+', input_file.readline().strip())]
            
        return earliest_timestamp, bus_lines

def get_input_2():
    with open('day13\input.txt', 'r') as input_file:
        earliest_timestamp = int(input_file.readline().strip())
        bus_lines = input_file.readline().strip().split(',')
            
        return bus_lines

def get_timestamp_for_line(earliest_timestamp, bus_line):
    return bus_line * math.ceil(earliest_timestamp / bus_line)

def get_answer_1():
    earliest_timestamp, bus_lines = get_input()
    timestamps = {}
    for bus_line in bus_lines:
        timestamps[bus_line] = get_timestamp_for_line(earliest_timestamp, bus_line)
    pprint.pprint(timestamps)
    minval = min(timestamps.values())
    bus_line = [key for key, value in timestamps.items() if value==minval][0]
    print((minval - earliest_timestamp) * bus_line)

def get_answer_2():
    bus_lines = get_input_2()
    # mult = 1
    # for index, bus_line in enumerate(bus_lines):
    #     if bus_line != 'x':
    #         print(index, bus_line)
    #         mult *= int(bus_line)

    # print(mult)
    
    # first_timestamps = []
    # for bus_line in bus_lines:
    #     try:
    #         first_timestamps.append(int(bus_line) * math.floor(100000000000000 / int(bus_line)))
    #     except:
    #         first_timestamps.append(None)
    # print(first_timestamps)
    print(bus_lines)

    # iterar por numero de lineas
    # para cada linea, tener en cuenta las lineas anteriores
    # buscar por fuerza bruta el match entre las dos primeras lineas
    # a partir de ahi, sumar periodos de mcm(linea1, linea2) y encontrar el match para la linea3
    
    for i in range(100000):
        timestamp = 37989391978419 + 47206096900157 * i
        if all(bus_line_meets_condition(timestamp, index, bus_line) for index, bus_line in enumerate(bus_lines)):
            print(timestamp)
            return

    # for i in range(100000000):
    #     timestamp = 779 + int(bus_lines[0]) * i
    #     if all(bus_line_meets_condition(timestamp, index, bus_line) for index, bus_line in enumerate(bus_lines)):
    #         print(timestamp)
    #         return

def search_min_match(initial_value, bus_lines):
    for i in range(100000000):
        timestamp = initial_value + int(bus_lines[0]) * i
        if all(bus_line_meets_condition(timestamp, index, bus_line) for index, bus_line in enumerate(bus_lines)):
            return timestamp

def bus_line_meets_condition(timestamp, index, bus_line):
    if index == 0:
        return True
    elif bus_line == 'x':
        return True
    else:
        return (timestamp + index) % int(bus_line) == 0

def main():
    get_answer_2()

if __name__ == '__main__':
    main()