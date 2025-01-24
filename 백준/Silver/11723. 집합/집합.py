import sys
input = sys.stdin.readline
n = int(input())
lst = []

for _ in range(n):
    ord = input().strip()
    if ' ' in ord:
        ord, k = ord.split()
        
    if ord == 'add':
        if int(k) in lst:
            pass
        else:
            lst.append(int(k))
    if ord == 'remove':
        if int(k) in lst:
            lst.remove(int(k))
        else:
            pass
    if ord == 'check':
        if int(k) in lst:
            print(1)
        else:
            print(0)
    if ord == 'toggle':
        if int(k) in lst :
            lst.remove(int(k))
        else:
            lst.append(int(k))
    if ord == 'all':
        lst = set([i for i in range(1, 21)])
    if ord == 'empty':
        lst = []