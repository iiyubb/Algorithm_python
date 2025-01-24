import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input().strip()))

lst.sort()
sum = 0
for a in lst:
    sum += a
print(round(sum / n))
print(lst[n//2])

dic = dict()
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_num = max(dic.values())
max_arr = []
for i in dic:
    if max_num == dic[i]:
        max_arr.append(i)
if len(max_arr) > 1:
    print(max_arr[1])
else: print(max_arr[0])
    
print(lst[-1] - lst[0])