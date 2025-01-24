def recur(idx, weight):
    
    if weight > k:
        return -9999999
    
    if idx == n:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    dp[idx][weight] = max(recur(idx+1, weight+table[idx][0])+table[idx][1], recur(idx+1, weight))

    return dp[idx][weight]
n, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100001)] for _ in range(n)]

print(recur(0,0))
