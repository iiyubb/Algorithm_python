n, k = map(int, input().split())
lst = list(map(int, input().split()))
prefix = [0 for _ in range(n+1)]
ans = []

for i in range(n):
    prefix[i+1] = prefix[i] + lst[i]

for j in range(k, n+1):
    ans.append(prefix[j] - prefix[j-k])

print(max(ans))