class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
def compute_tree_height(node):
    if not node.children:
        return 1
    child_heights = [compute_tree_height(child) for child in node.children]
    return max(child_heights) + 1
def main():
    input_format = input("")
    num_nodes = 0
    parent_indices = []
    if "I" in input_format:
        num_nodes = input("")
        num_nodes = int(num_nodes.replace("\\r\\n", ""))
        print(num_nodes)
        parent_indices = list(map(int, input("").split()))
    else:
        file_path = input("")
        while "z" in file_path:
            file_path = input("")
        with open(f"./data/{file_path}", "r") as file:
            num_nodes = int(file.readline())
            parent_indices = list(map(int, file.readline().split()))
    nodes = [TreeNode(i) for i in range(num_nodes)]
    root = None
    for i, parent_index in enumerate(parent_indices):
        if parent_index == -1:
            root = nodes[i]
        else:
            nodes[parent_index].children.append(nodes[i])
    tree_height = compute_tree_height(root)
    print(tree_height)
