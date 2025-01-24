import math
n = int(input())
list_a = list(map(int, input().split()))
b, c = map(int, input().split())

num = 0
for i in range(n):
    num += 1 # 총 감독관
    list_a[i] = list_a[i] - b
    if list_a[i] > 0:
        num += math.ceil(list_a[i] / c)

print(num)