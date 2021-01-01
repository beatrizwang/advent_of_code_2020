import re
import pprint
import copy

def get_instructions():
    with open('day12\input.txt', 'r') as input_file:
        inputText = input_file.read()
        lines = inputText.split('\n')
        return [[line[0], int(line[1:])] for line in lines]

def apply_instruction(position, direction, instruction):
    action = instruction[0]
    value = instruction[1]
    if instruction[0] == 'N' or (instruction[0] == 'F' and direction == 'N'):
        position[1] += value
    elif instruction[0] == 'S' or (instruction[0] == 'F' and direction == 'S'):
        position[1] -= value
    elif instruction[0] == 'E' or (instruction[0] == 'F' and direction == 'E'):
        position[0] += value
    elif instruction[0] == 'W' or (instruction[0] == 'F' and direction == 'W'):
        position[0] -= value
    elif instruction[0] == 'L' or instruction[0] == 'R':
        direction = get_new_direction(direction, instruction)
    return position, direction

def get_new_direction(direction, instruction):
    action = instruction[0]
    value = instruction[1]
    directions = ['N', 'E', 'S', 'W']
    index = directions.index(direction)
    if action == 'R':
        new_index = int((index + (value / 90)) % 4)
    elif action == 'L':
        new_index = int((index - (value / 90)) % 4)
    return directions[new_index]

def get_answer_1():
    instructions = get_instructions()
    position = [0,0]
    direction = 'E'
    for instruction in instructions:
        position, direction = apply_instruction(position, direction, instruction)
    print(abs(position[0]) + abs(position[1]))

def apply_instruction_2(position, position_waypoint, instruction):
    action = instruction[0]
    value = instruction[1]
    if instruction[0] == 'N':
        position_waypoint[1] += value
    elif instruction[0] == 'S':
        position_waypoint[1] -= value
    elif instruction[0] == 'E':
        position_waypoint[0] += value
    elif instruction[0] == 'W':
        position_waypoint[0] -= value
    elif instruction[0] == 'L' or instruction[0] == 'R':
        position_waypoint = get_new_position_waypoint(position, position_waypoint, instruction)
    elif instruction[0] == 'F':
        position, position_waypoint = move_forward_waypoint(position, position_waypoint, instruction)
    return position, position_waypoint

def get_new_position_waypoint(position, position_waypoint, instruction):
    action = instruction[0]
    value = instruction[1]

    if value == 180:
        return [position[0] - (position_waypoint[0] - position[0]), position[1] - (position_waypoint[1] - position[1])]
    elif (action == 'R' and value == 90) or (action == 'L' and value == 270):
        return [position[0] + (position_waypoint[1] - position[1]), position[1] - (position_waypoint[0] - position[0])]
    elif (action == 'L' and value == 90) or (action == 'R' and value == 270):
        return [position[0] - (position_waypoint[1] - position[1]), position[1] + (position_waypoint[0] - position[0])]

def move_forward_waypoint(position, position_waypoint, instruction):
    action = instruction[0]
    value = instruction[1]

    relative_x = position_waypoint[0] - position[0]
    relative_y = position_waypoint[1] - position[1]

    position = [position[0] + value * relative_x, position[1] + value * relative_y]
    position_waypoint = [position[0] + relative_x, position[1] + relative_y]
    return position, position_waypoint

def get_answer_2():
    instructions = get_instructions()
    position = [0,0]
    position_waypoint = [10,1]
    for instruction in instructions:
        position, position_waypoint = apply_instruction_2(position, position_waypoint, instruction)
        print(position, position_waypoint)
    print(abs(position[0]) + abs(position[1]))

def main():
    get_answer_2()

if __name__ == '__main__':
    main()