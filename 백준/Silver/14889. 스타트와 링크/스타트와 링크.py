import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

visit = [False for _ in range(n)]
ans = 999999999

def recur(L, idx):
    global ans
    if L == n // 2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if (visit[i] and visit[j]):
                    a += lst[i][j]
                elif not visit[i] and not visit[j]:
                    b += lst[i][j]
        ans = min(ans, abs(a-b))
        return
    
    for i in range(idx, n):
        if not visit[i]:
            visit[i] = True
            recur(L+1, i+1)
            visit[i] = False

recur(0,0)
print(ans)         
        