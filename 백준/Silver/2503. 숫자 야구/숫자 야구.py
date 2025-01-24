import sys
sys.setrecursionlimit(9999999)

n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def checker(hind_idx, num):
    strike = 0
    ball = 0
    
    right = hint[hind_idx][0]
    right_strike = hint[hind_idx][1]
    right_ball = hint[hind_idx][2]
    
    right_fir = right // 100
    right_sec = (right % 100) // 10
    right_thi = (right % 100) % 10
    
    num_fir = num // 100
    num_sec = (num % 100) // 10
    num_thi = (num % 100) % 10
    
    if (num_fir == num_sec) or (num_sec == num_thi) or (num_thi == num_fir):
        return False
    
    if (num_sec == 0) or (num_thi == 0):
        return False
    
    if num_fir == right_fir:
        strike += 1
    if num_sec == right_sec:
        strike += 1
    if num_thi == right_thi:
        strike += 1
        
    if (num_fir == right_sec) or (num_fir == right_thi):
        ball += 1
    if (num_sec == right_fir) or (num_sec == right_thi):
        ball += 1
    if (num_thi == right_fir) or (num_thi == right_sec):
        ball += 1
        
    if (strike == right_strike) and (ball == right_ball):
        return True

def recur(hint_idx, num):
    global answer
    if (hint_idx == n):
        answer += 1
        recur(0, num+1)
        return
    
    if (num == 988):
        return
    
    if checker(hint_idx, num):
        recur(hint_idx+1, num)
    else:
        recur(0, num+1)

recur(0, 100)
print(answer)