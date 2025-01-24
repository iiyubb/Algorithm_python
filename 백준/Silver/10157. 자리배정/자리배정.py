c, r = map(int, input().split())
k = int(input())
arr = [[False]*c for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
num = 1
x, y = 0, 0
i = 0

if k > c*r:
    print(0)

else:
    while True:
        if num == k:
            print(x + 1, y + 1)
            exit()

        arr[y][x] = True
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r:
            if arr[ny][nx]:
                i = (i+1) % 4
            else:
                x, y = nx, ny
                num += 1
        else:
            i = (i+1) % 4
