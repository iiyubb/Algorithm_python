import sys
input = sys.stdin.readline
arr = sorted([int(input()) for _ in range(9)])
deli = sum(arr) - 100
delete = []
for i in range(9):
    for j in range(i+1, 9):
        if len(delete) == 2:
            continue
        if arr[i] + arr[j] == deli:
            delete.append(arr[i])
            delete.append(arr[j])
            break

for a in arr:
    if a in delete:
        continue
    else:
        print(a)