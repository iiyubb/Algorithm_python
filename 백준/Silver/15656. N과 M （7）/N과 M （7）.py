n, m = map(int, input().split())
in_arr = [int(i) for i in input().split()]

arr = []
def recur(num):
    if (num == m):
        print(*arr)
        return
    
    for i in sorted(in_arr):
        arr.append(i)
        recur(num+1)
        arr.pop()
        
recur(0)