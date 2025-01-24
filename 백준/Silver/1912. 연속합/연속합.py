n = int(input())
arr = list(map(int, input().split()))
prefix = [-1001 for _ in range(n+1)]


maxnum = 0
for k in range(n):
    prefix[k+1] = max(prefix[k]+arr[k], arr[k])
print(max(prefix))