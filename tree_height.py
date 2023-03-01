def compute_height(n, parents):
    tree = [[] for i in range(n)]
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    height = 0
    queue = [root]
    while len(queue) > 0:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            for child in tree[node]:
                queue.append(child)
        height += 1
    return height
