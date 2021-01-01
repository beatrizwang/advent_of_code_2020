import re
import pprint

def get_answers_groups():
    with open('day6\input.txt', 'r') as input_file:
        inputText = input_file.read()
        return (inputText.split('\n\n'))

def get_points_group_any(answers_group):
    answers_group = answers_group.replace('\n', '')
    return len(list(set(answers_group)))

def get_points_group_all(answers_group):
    answers = answers_group.split('\n')
    answers_set = [set(answer) for answer in answers]
    intersection = set.intersection(*answers_set) 
    return len(intersection)

def main():
    answers_groups = get_answers_groups()
    # points_any = [get_points_group_any(group) for group in answers_groups]
    # print(sum(points_any))

    points_all = [get_points_group_all(group) for group in answers_groups]
    print(sum(points_all))

if __name__ == '__main__':
    main()