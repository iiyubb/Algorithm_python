import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    comm = input().strip()

    if ' ' in comm:
        comm, k = comm.split()

    if comm == 'push':
        stack.append(int(k))
    if comm == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    if comm == 'size':
        print(len(stack))    
    if comm == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if comm == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack = stack[:-1]
