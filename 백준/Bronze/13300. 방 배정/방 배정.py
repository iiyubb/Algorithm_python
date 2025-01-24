import math
n, k = map(int, input().split())
cnt = 0
arr = [[0] * 2 for _ in range(6)]

for i in range(n):
    gen, grade = map(int, input().split())
    arr[grade-1][gen] += 1

for i in range(6):
    for j in range(2):
        cnt += math.ceil(arr[i][j] / k)

print(cnt)