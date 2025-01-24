n = int(input())
paper = [list([0 for _ in range(1001)]) for _ in range(1001)]

for i in range(1, n+1):
    start_x, start_y, x, y = map(int, input().split())
    for w in range(x):
        for h in range(y):
            paper[start_y+h][start_x+w] = i

for k in range(1, n+1):
    count = 0
    for w in range(1001):
        for h in range(1001):
            if paper[h][w] == k:
                count += 1
    print(count)