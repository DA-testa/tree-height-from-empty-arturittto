def compute_height(node, height, visited):
    visited.add(node)
    max_height = height
    for child in node:
        if child not in visited:
            child_height = compute_height(node[child], height + 1, visited)
            max_height = max(max_height, child_height)
    return max_height
def main():
    input_type = input("").strip()
    n = 0
    parents = []
    if input_type == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        file_path = input().strip()
        while "a" in file_path:
            file_path = input().strip()
        with open(f"./test/{file_path}", "r") as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    nodes = {i: [] for i in range(n)}
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)
    height = compute_height(nodes, 1, set([root]))
    print(height)
import sys
import threading
sys.setrecursionlimit(100000)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
