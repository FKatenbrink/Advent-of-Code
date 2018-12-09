import sys
import re
import itertools


def test_day7_1():
    assert line_to_connection(
        "Step F must be finished before step E can begin.") == ("F", "E")
    assert day7_1(
        "Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin."
    ) == "CABDFE"
    print("All tests successful.")


class Node:

    def __init__(self, letter, next_node=None):
        self.letter = letter
        self.next_nodes = []
        if next_node:
            self.add_next(next_node)

    def add_next(self, next_node):
        self.next_nodes.append(next_node)


def line_to_connection(line):
    # Step L must be finished before step D can begin.
    regex = r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."
    match = re.search(regex, line)
    before = match.group(1)
    after = match.group(2)
    return (before, after)


def next_root(root_nodes, graph):
    for node in root_nodes:
        non_root_nodes = [
            graph[n] for n in root_nodes if n != node and n in graph
        ]
        if node not in set(itertools.chain(*non_root_nodes)):
            return node


def day7_1(input):
    lines = input.split("\n")
    connections = [line_to_connection(line) for line in lines]
    graph = {}
    non_root_nodes = set()
    for con in connections:
        node = con[0]
        next_node = con[1]
        if node in graph:
            graph[node].add(next_node)
        else:
            graph[node] = set(next_node)
        non_root_nodes.add(next_node)
    root_nodes = set(graph.keys()) - non_root_nodes
    result = ""
    while len(root_nodes) > 0:
        node = next_root(sorted(root_nodes), graph)
        result += node
        root_nodes.remove(node)
        if node in graph:
            root_nodes.update(graph[node])
    return result


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day7_1(file.read().strip())}")
    else:
        test_day7_1()
