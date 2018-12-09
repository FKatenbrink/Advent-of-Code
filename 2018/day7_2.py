import sys
import re
import itertools


def test_day7_1():
    assert line_to_connection(
        "Step F must be finished before step E can begin.") == ("F", "E")
    result = day7_1(
        "Step C must be finished before step A can begin.\nStep C must be finished before step F can begin.\nStep A must be finished before step B can begin.\nStep A must be finished before step D can begin.\nStep B must be finished before step E can begin.\nStep D must be finished before step E can begin.\nStep F must be finished before step E can begin.",
        2)
    assert result == ("CABFDE", 15), "Result: " + str(result)
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
    return None


def node_to_seconds(node):
    return ord(node) - ord("A") + 1 + 60


def idle_worker_index(workers):
    for idx, w in enumerate(workers):
        if w[0] is None:
            return idx
    return None


def day7_1(input, worker_num=5):
    lines = input.split("\n")
    connections = [line_to_connection(line) for line in lines]
    graph = {}
    reverse_graph = {}
    non_root_nodes = set()
    for con in connections:
        node = con[0]
        next_node = con[1]
        if node in graph:
            graph[node].add(next_node)
        else:
            graph[node] = set(next_node)
        if next_node in reverse_graph:
            reverse_graph[next_node].add(node)
        else:
            reverse_graph[next_node] = set(node)
        non_root_nodes.add(next_node)
    root_nodes = set(graph.keys()) - non_root_nodes

    order = ""
    time = 0
    visited_nodes = set()
    workers = [[None, 0] for i in range(worker_num)]
    while len(root_nodes) > 0 or any([w[0] for w in workers]):
        while True:
            node = next_root(sorted(root_nodes), graph)
            worker_index = idle_worker_index(workers)
            if node is not None and worker_index is not None:
                root_nodes.remove(node)
                workers[worker_index] = [node, node_to_seconds(node)]
            else:
                break

        for idx, worker in enumerate(workers):
            node = worker[0]
            if node is not None:
                if worker[1] > 1:
                    worker[1] -= 1
                else:
                    if node in graph:
                        visited_nodes.add(node)
                        new_nodes = graph[node] - visited_nodes
                        new_nodes -= set(
                            new_node for new_node in new_nodes if any(
                                map(lambda n: n not in visited_nodes,
                                    reverse_graph[new_node])))
                        root_nodes.update(new_nodes)
                    order += node
                    workers[idx] = [None, 0]
        time += 1
        t = 0

    return (order, time)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day7_1(file.read().strip())}")
    else:
        test_day7_1()
