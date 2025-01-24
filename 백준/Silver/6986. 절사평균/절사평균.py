import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(float(input().strip()))
    
def mean(arr):
    return sum(arr) / len(arr)

arr.sort()
if k == 0:
    mean1 = mean(arr)
else:
    mean1 = mean(arr[k:-k])

for i in range(k):
    arr[i] = arr[k]
    arr[-(i+1)] = arr[-(k+1)]
mean2 = mean(arr)

print(f'{mean1+0.00000001:.2f}')
print(f'{mean2+0.00000001:.2f}')