n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
ans = []
idx = 0

for t in range(n):
    idx += k-1
    if idx >= len(lst):
        idx = idx % len(lst)
        
    ans.append(str(lst.pop(idx)))
print("<" + ", ".join(ans) + ">")
        