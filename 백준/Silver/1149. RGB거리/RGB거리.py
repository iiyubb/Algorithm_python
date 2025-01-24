n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(3)] for _ in range(n)]

for k in range(3):
    dp[0][k] = graph[0][k]
    
for idx in range(1, n):
    for RGB in range(3):
        
        if RGB == 0: # Red
            dp[idx][RGB] = min(dp[idx-1][1], dp[idx-1][2]) + graph[idx][RGB]
        if RGB == 1: # Green
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][2]) + graph[idx][RGB]
        if RGB == 2: # Blue
            dp[idx][RGB] = min(dp[idx-1][0], dp[idx-1][1]) + graph[idx][RGB]
            
print(min(dp[-1]))