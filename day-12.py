class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = set()
        self.is_small = val.lower() == val

with open('input.txt') as f:
    edges = [x for x in f.read().split('\n') if x != '']

GRAPH_NODES = {}
for edge in edges:
    n1, n2 = edge.split('-')
    if n1 not in GRAPH_NODES: GRAPH_NODES[n1] = Node(n1)
    if n2 not in GRAPH_NODES: GRAPH_NODES[n2] = Node(n2)
    n1, n2 = GRAPH_NODES[n1], GRAPH_NODES[n2]
    n1.neighbours.add(n2)
    n2.neighbours.add(n1)


def part_1():
    def find_paths(visited, current_node):
        if current_node in visited: return 0
        if current_node.val == 'end': return 1
        if current_node.is_small: visited = set.union(visited, {current_node})
        return sum([find_paths(visited, neighbour) for neighbour in current_node.neighbours])

    return find_paths(set(), GRAPH_NODES['start'])

def part_2():
    def find_paths(visited, current_node, visited_twice):
        if current_node.val == 'end': return 1
        if current_node in visited_twice: return 0
        if len(visited_twice) > 1 and current_node in visited: return 0
        if current_node.is_small: 
            if current_node in visited: visited_twice = set.union(visited_twice, {current_node})
            else: visited = set.union(visited, {current_node})
        return sum([find_paths(visited, neighbour, visited_twice) for neighbour in current_node.neighbours])

    return find_paths({GRAPH_NODES['start']}, GRAPH_NODES['start'], set())


print("PART 1: ", part_1())
print("PART 2: ", part_2())

