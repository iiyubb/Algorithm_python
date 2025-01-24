import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    order = input().strip()
    if " " in order:
        order, k = order.split()
    
    if order == 'push':
        arr.append(int(k))
    if order == 'pop':
        if len(arr):
            print(arr[0])
            arr.pop(0)
        else:
            print(-1)
    if order == 'size':
        print(len(arr))
    if order == 'empty':
        if len(arr):
            print(0)
        else:
            print(1)
    if order == 'front':
        if len(arr):
            print(arr[0])
        else:
            print(-1)
    if order == 'back':
        if len(arr):
            print(arr[-1])
        else:
            print(-1)
    