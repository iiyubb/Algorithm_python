n = int(input())
arr = list(map(int, input().split()))

ans1 = [1] * n
ans2 = [1] * n

for i in range(n-1):
    if arr[i] >= arr[i+1]:
        ans1[i+1] += ans1[i]

for i in range(n-1):
    if arr[i] <= arr[i+1]:
        ans2[i+1] += ans2[i]

max1 = max(ans1)
max2 = max(ans2)

print(max(max1, max2))