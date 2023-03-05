import numpy
import threading
import sys

def compute_tree_height(n_nodes: int, parents: np.ndarray) -> int:
    tree = [[] for i in range(n_nodes)]
    root = -1
    for i in range(n_nodes):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    height = 0
    queue = [root]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            for child in tree[node]:
                queue.append(child)
        height += 1
    return height


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def compute_tree_height_recursive(node):
    if not node.children:
        return 1
    heights = [compute_tree_height_recursive(child) for child in node.children]
    return max(heights) + 1


def main():
    input_type = input("")
    n_nodes = 0
    parents = np.array([])
    if "I" in input_type:
        n_nodes = int(input(""))
        parents = np.array(list(map(int, input("").split())))
    else:
        file_path = input("")
        while "a" in file_path:
            file_path = input("")
        with open(f"./test/{file_path}", "r") as file:
            n_nodes = int(file.readline())
            parents = np.array(list(map(int, file.readline().split())))

    height = compute_tree_height(n_nodes, parents)
    print(height)


numpy.set_printoptions(threshold=numpy.inf)
threading.stack_size(2**27)
threading.Thread(target=main).start()
sys.setrecursionlimit(10**7)
