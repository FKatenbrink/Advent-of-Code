import sys


def test_day8_1():
    result = day8_1("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    assert result == 138, "Result: " + str(result)
    print("All tests successful.")


class Node:

    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        self.children.extend(children)

    def add_metadata(self, metadata):
        self.metadata.append(metadata)

    def add_metadatas(self, metadatas):
        self.metadata.extend(metadatas)


def parse_input():
    num_children = input_list.pop(0)
    num_metadata = input_list.pop(0)
    node = Node()
    node.add_children([parse_input() for _ in range(num_children)])
    node.add_metadatas(input_list.pop(0) for _ in range(num_metadata))
    return node


def metadata_sum(node):
    return sum(node.metadata) + sum([metadata_sum(c) for c in node.children])


def day8_1(input):
    global input_list
    input_list = list(map(int, input.split(" ")))
    root_node = parse_input()
    return metadata_sum(root_node)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            print(f"Result for file input: {day8_1(file.read().strip())}")
    else:
        test_day8_1()
