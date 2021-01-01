import re
import pprint
import itertools

def get_numbers():
    with open('day10\input.txt', 'r') as input_file:
        inputText = input_file.read()
        return [int(line) for line in inputText.split('\n')]

def get_differences(numbers):
    differences = []
    differences.append(numbers[0])
    for index in range(len(numbers) - 1):
        differences.append(numbers[index + 1] - numbers[index])
    differences.append(3)
    return differences

def get_answer_1(numbers):
    diffs = get_differences(numbers)
    return diffs.count(1) * diffs.count(3)

# def get_answer_2(numbers):

def create_graph(numbers):
    graph = {}
    numbers.insert(0,0)
    numbers.append(max(numbers) + 3)

    for number in numbers:
        graph[number] = [number + i for i in [1,2,3] if number + i in numbers]
    return graph

def main():
    numbers = get_numbers()
    numbers.sort()
    graph = create_graph(numbers)
    needed_nodes = [value[0] for key, value in graph.items() if len(value) == 1]
    needed_nodes.append(0)
    numbers_combination = [number for number in numbers if number not in needed_nodes]
    # larger_nodes = { key: value for key, value in graph.items() if len(value) > 1 }
    pprint.pprint(numbers_combination)
    

if __name__ == '__main__':
    main()