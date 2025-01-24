n = int(input())
list_a = list(map(int, input().split()))
num = list(map(int, input().split()))

ans_min = 1000000000
ans_max = -1000000000

def recur(idx, tmp):
    global ans_min
    global ans_max
    
    if idx == n-1:
        ans_min = min(tmp, ans_min)
        ans_max = max(tmp, ans_max)
        return
    
    if num[0] > 0:
        num[0] -= 1
        recur(idx+1, tmp+list_a[idx+1])
        num[0] += 1
    
    if num[1] > 0:
        num[1] -= 1
        recur(idx+1, tmp-list_a[idx+1])
        num[1] += 1
        
    if num[2] > 0:
        num[2] -= 1
        recur(idx+1, tmp*list_a[idx+1])
        num[2] += 1
        
    if num[3] > 0:
        num[3] -= 1
        recur(idx+1, int(tmp/list_a[idx+1]))
        num[3] += 1
        
recur(0, list_a[0])
print(ans_max)
print(ans_min)