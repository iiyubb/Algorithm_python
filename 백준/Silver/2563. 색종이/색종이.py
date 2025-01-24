import sys
input = sys.stdin.readline

n = int(input())

area = [list(0 for _ in range(101)) for _ in range(101)]

for i in range(n):
    x1, y1 = map(int, input().split())
    x2, y2 = x1 + 10, y1 + 10
    for c in range(x1, x2):
        for r in range(y1, y2):
            area[r][c] = 1

cnt = 0 
for i in range(101):
    for j in range(101):
        if area[i][j] == 1:
            cnt += 1
            
print(cnt)