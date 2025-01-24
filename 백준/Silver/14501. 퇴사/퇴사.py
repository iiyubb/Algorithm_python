### 바텀업 DP (점화식)

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

for idx in range(n)[::-1]:
    
    if idx + table[idx][0] > n:
        dp[idx] = dp[idx+1]
    else:
        dp[idx] = max( dp[idx+table[idx][0]] + table[idx][1], dp[idx+1] )

print(dp[0])
