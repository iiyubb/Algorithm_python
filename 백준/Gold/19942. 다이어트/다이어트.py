def recur(idx, p, f, s, v, price):
    global answer
    global used
    global answer_used
    
    if (p >= mp) and (f >= mf) and (s >= ms) and (v >= mv) and (price < answer):
        answer = min(answer, price)
        answer_used = []
        for i in used:
            answer_used.append(i)
        return
    if idx == n:
        return
    
    used.append(idx+1)
    
    recur(idx+1, p+ing[idx][0], f+ing[idx][1], s+ing[idx][2], v+ing[idx][3], price+ing[idx][4])
    used.pop()
    
    recur(idx+1, p, f, s, v, price)
    
n = int(input())
mp, mf, ms, mv = map(int, input().split())
ing = [list(map(int, input().split())) for _ in range(n)]

answer = 999999
used = []
answer_used = []

recur(0,0,0,0,0,0)
if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)
