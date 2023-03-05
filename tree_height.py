import sys
import threading
import numpy as np

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def compute_height(n, parents):
    root_node = None
    nodes = [TreeNode(i) for i in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            root_node = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    queue = [root_node]
    height = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
        height += 1
    return height

def main():
    input_type = input("")
    n = 0
    parents = []
    if "I" in input_type:
        n = int(input(""))
        parents = list(map(int, input("").split()))
        print(compute_height(n, parents))
    else:
        file_path = input("")
        while "a" in file_path:
            file_path = input("")
        with open(f"./test/{file_path}", "r") as file:
            n = int(file.readline())
            parents = list(map(int, file.readline().split()))

        height = compute_height(n, parents)
        print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
