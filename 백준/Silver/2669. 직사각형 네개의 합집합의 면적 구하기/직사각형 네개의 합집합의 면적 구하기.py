import sys
input = sys.stdin.readline

area = [list(0 for _ in range(101)) for _ in range(101)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            area[r][c] = 1

cnt = 0
for row in area:
    cnt += sum(row)
    
print(cnt)