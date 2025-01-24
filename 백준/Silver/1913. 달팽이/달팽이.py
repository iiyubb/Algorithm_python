n = int(input())
k = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
i, j = 0, 0
num = n**2
print_i = 0
print_j = 0

for ll in range((n+1)//2):
    start_i, start_j = ll, ll
    
    for i in range(start_i, n):
        j = start_j
        arr[i][j] = num
        if num == k:
            print_i, print_j = i, j
        num -= 1
    
    for j in range(start_j+1, n):
        arr[i][j] = num
        if num == k:
            print_i, print_j = i, j
        num -= 1
        
    for i in range(n-2, start_i-1, -1):
        arr[i][j] = num
        if num == k:
            print_i, print_j = i, j
        num -= 1
    
    for j in range(n-2, start_j, -1):
        arr[i][j] = num
        if num == k:
            print_i, print_j = i, j
        num -= 1
        
    n -= 1
    
for i in range(len(arr)):
    print(*arr[i])
print(print_i+1, print_j+1)