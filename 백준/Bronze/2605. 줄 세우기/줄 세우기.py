n = int(input())
arr = list(map(int, input().split()))
line = []

for i in range(n):
    if arr[i] > 0:
        idx = line.index(1)
        line.insert(-arr[i], i+1)
    elif arr[i] == 0:
        line.insert(i, i+1)

print(*line)