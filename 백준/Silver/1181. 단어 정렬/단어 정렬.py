import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    arr.append(input().strip())

arr = list(set(arr))
arr.sort()
arr.sort(key = lambda x:(len(x), ord(x[0])))

print("\n".join(arr))