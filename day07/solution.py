import re
import pprint

regExBags = '[a-z]+ [a-z]+ bags'
# regExBag = '[a-z]+ [a-z]+ bag'
regExBag = '\d+ [a-z]+ [a-z]+ bag'

def read_input():
    f = open('day7\input.txt', 'r')
    inputText = f.read()

    coincidences = [c.group() for c in re.finditer(regExBags, inputText)]
    coincidences_diff = list(set(coincidences))
    coincidences_diff.remove('no other bags')

    output = open('day7\\bags.txt', 'w')
    for distinct_bag in coincidences_diff:
        output.write(distinct_bag)
        output.write('\n')

    f.close()
    output.close()

def create_graph():
    graph = {}
    input_file = open('day7\input.txt', 'r')
    inputText = input_file.read()

    with open('day7\\bags.txt', 'r') as bags_file:
        for line in bags_file:
            line = line.rstrip()
            regExp = line + ' contain [^.]+'
            content = re.search(regExp, inputText)
            if content:
                indexContain = content.group().find('contain')
                destNodes = re.findall(regExBag, content.group()[indexContain:])
                if len(destNodes) > 0:
                    graph[line.replace('bags', 'bag')] = destNodes

    input_file.close()
    # pprint.pprint(graph)
    return graph

def create_weighted_graph():
    graph = {}
    input_file = open('day7\input.txt', 'r')
    inputText = input_file.read()

    with open('day7\\bags.txt', 'r') as bags_file:
        for line in bags_file:
            line = line.rstrip()
            regExp = line + ' contain [^.]+'
            content = re.search(regExp, inputText)
            if content:
                indexContain = content.group().find('contain')
                destNodes = re.findall(regExBag, content.group()[indexContain:])
                if len(destNodes) > 0:
                    graph[line.replace('bags', 'bag')] = [(re.search('[a-z]+ [a-z]+ bag', node).group(), re.search('\d+', node).group()) for node in destNodes]

    input_file.close()
    # pprint.pprint(graph)
    return graph

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def count_possible_starts():
    graph = create_graph()
    counter = 0

    # path = find_path(graph, 'shiny gold bag', 'shiny gold bag')
    # print(path)
    with open('day7\\bags.txt', 'r') as bags_file:
        for line in bags_file:
            line = line.rstrip().replace('bags', 'bag')
            path = find_path(graph, line, 'shiny gold bag')
            if path != None:
                counter += 1
    print(counter)

def count_number_bags_inside(graph, bag_color):
    number = 0
    for content_color in graph[bag_color]:
        if content_color[0] in graph:
            number += int(content_color[1]) * count_number_bags_inside(graph, content_color[0])
        
        number += int(content_color[1])

    return number
    #     path = find_path(graph, line, 'shiny gold bag')

def main():
    graph = create_weighted_graph()
    count = count_number_bags_inside(graph, 'shiny gold bag')
    print(count)

if __name__ == '__main__':
    main()