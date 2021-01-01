import re
import pprint

def get_instructions():
    with open('day8\input.txt', 'r') as input_file:
        inputText = input_file.read()
        return (inputText.split('\n'))

def get_instructions_with_count():
    instructions = get_instructions()
    return [[instruction[0:3], int(instruction[4:]), 0] for instruction in instructions]

def count_until_rep(instructions):
    index = 0
    accumulator = perform_action(index, instructions, 0)
    return accumulator


def perform_action(index, instructions, accumulator):
    if index >= len(instructions):
        return accumulator

    if instructions[index][2] > 0:
        return accumulator
    else:
        instructions[index][2] = 1

    if instructions[index][0] == 'jmp':
        return perform_action(index + instructions[index][1], instructions, accumulator)
    elif instructions[index][0] == 'acc':
        accumulator += instructions[index][1]
        return perform_action(index + 1, instructions, accumulator)
    elif instructions[index][0] == 'nop':
        return perform_action(index + 1, instructions, accumulator)


def get_next_index(index, instructions): 
    if instructions[index][0] == 'jmp':
        return index + instructions[index][1]
    return index + 1

def detect_loop(index, instructions):
    if instructions[index][2] > 0:
        return True
    else:
        instructions[index][2] = 1

    if instructions[index][0] == 'jmp':
        return detect_loop(index + instructions[index][1], instructions)
    elif instructions[index][0] == 'acc':
        return detect_loop(index + 1, instructions)
    elif instructions[index][0] == 'nop':
        return detect_loop(index + 1, instructions)

def has_loop(instructions):
    index = 0
    has_loop = False
    try:
        has_loop = detect_loop(index, instructions)
    except:
        return False
    return has_loop

def detect_wrong_line():
    instructions = get_instructions_with_count()
    for index in range(0, len(instructions)):
        instructions_altered = get_instructions_with_count()
        if instructions[index][0] == 'jmp':
            instructions_altered[index][0] = 'nop'
            if not has_loop(instructions_altered):
                return True

        if instructions[index][0] == 'nop':
            instructions_altered[index][0] = 'jmp'
            if not has_loop(instructions_altered):
                return True

def main():
    instructions = get_instructions_with_count()
    # count = count_until_rep(instructions)
    # wrong_instruction = detect_wrong_line()
    # print(wrong_instruction) #226

    instructions[226][0] = 'nop'
    count = count_until_rep(instructions)
    print(count)

if __name__ == '__main__':
    main()