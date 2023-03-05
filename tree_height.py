import sys
import threading

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def calculate_tree_height(node):
    if not node.children:
        return 1
    heights = [calculate_tree_height(child) for child in node.children]
    return max(heights) + 1


def main():
    input_method = input("")
    num_nodes = 0
    parents = []
    if "I" in input_method:
        num_nodes = input("")
        num_nodes = int(num_nodes.replace("\\r\\n",""))
        parents = list(map(int, input("").split()))
    else:
        file_path = input("")
        while "a" in file_path:
            file_path = input("")
        with open(f"./test/{file_path}", "r") as f:
            num_nodes = int(f.readline())
            parents = list(map(int, f.readline().split()))

    nodes = [TreeNode(i) for i in range(num_nodes)]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    tree_height = calculate_tree_height(root)
    print(tree_height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

