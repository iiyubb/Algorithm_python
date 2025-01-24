n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
sum = 0
max_length = [ll[1] for ll in arr]
max_idx = max_length.index(max(max_length))
max_loc = arr[max_idx][0]
end_loc = arr[-1][0]
start_loc = arr[0][0]
prev = 0

for i in range(max_idx):
    loc = arr[i][0]
    for l in range(loc, arr[i+1][0]):
        if arr[i][1] > prev:
            sum += arr[i][1]
            prev = arr[i][1]
        else:
            sum += prev

sum += arr[max_idx][1]

prev = 0
for k in range(1, n-max_idx):
    loc = arr[-k][0]
    for j in range(loc, arr[-k-1][0], -1):
        if arr[-k][1] > prev:
            sum += arr[-k][1]
            prev = arr[-k][1]
        else:
            sum += prev
print(sum)
