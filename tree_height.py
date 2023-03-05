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


def main():
    text = input()
    if text.startswith('I'):
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))
    elif text.startswith('F'):
        file = "./test/05"
        with open(file) as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
            print(compute_height(n, parents))
    else:
        print("Invalid input")
#1

if __name__ == "__main__":
    main()
