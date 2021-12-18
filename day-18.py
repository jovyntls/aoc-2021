with open('input.txt') as f:
    lines = [eval(x) for x in f.read().strip().split('\n')]

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Leaf:
    def __init__(self, val):
        self.val = val

class Tree:
    def __init__(self, node):
        self.root = node
        self.build_traversal()

    @staticmethod
    def build_tree(exp):
        def list_to_node(exp):
            if isinstance(exp, list): return Node(list_to_node(exp[0]), list_to_node(exp[1]))
            else: return Leaf(exp)
        root = list_to_node(exp)
        return Tree(root)

    def build_traversal(self):
        self.traversal = []
        self.in_order_traverse(self.root, 1)
        last_node = None
        for node in self.traversal:
            node.prev = last_node
            last_node = node
        next_node = None
        for node in reversed(self.traversal):
            node.next = next_node
            next_node = node

    def in_order_traverse(self, node, level):
        node.level = level
        if isinstance(node, Leaf): 
            self.traversal.append(node)
        else:
            node.left.parent = node
            node.right.parent = node
            self.in_order_traverse(node.left, level + 1)
            self.in_order_traverse(node.right, level + 1)

    def explode(self, node):
        if node.left.prev: node.left.prev.val += node.left.val
        if node.right.next: node.right.next.val += node.right.val
        if node == node.parent.left: node.parent.left = Leaf(0)
        else: node.parent.right = Leaf(0)
        self.build_traversal()

    def split(self, leaf):
        new_node = Node(Leaf(leaf.val//2), Leaf((leaf.val+1)//2))
        if leaf == leaf.parent.left: leaf.parent.left = new_node
        else: leaf.parent.right = new_node
        self.build_traversal()

    def simplify(self):
        for leaf in self.traversal:
            if leaf.level > 5:
                self.explode(leaf.parent)
                return self.simplify()
        for leaf in self.traversal:
            if leaf.val > 9:
                self.split(leaf)
                return self.simplify()
    
    def final_sum(self, node):
        if isinstance(node, Leaf): return node.val
        else: return 3*self.final_sum(node.left) + 2*self.final_sum(node.right)


def part_1():
    tree = Tree.build_tree(lines[0])
    for exp in lines[1:]:
        tree_to_add = Tree.build_tree(exp)
        tree = Tree(Node(tree.root, tree_to_add.root))
        tree.simplify()
    return tree.final_sum(tree.root)

def part_2():
    largest = 0
    for exp1 in lines:
        for exp2 in lines:
            if exp1 == exp2: continue
            subtree1 = Tree.build_tree(exp1)
            subtree2 = Tree.build_tree(exp2)
            tree = Tree(Node(subtree1.root, subtree2.root))
            tree.simplify()
            treesum = tree.final_sum(tree.root)
            if treesum > largest: largest = treesum
    return largest


print("PART 1: ", part_1())
print("PART 2: ", part_2())

