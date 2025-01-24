n = int(input())
dice = [list(map(int, input().strip().split())) for _ in range(n)]
rotate = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
ans = 0

def cal(num):
    result = 0
    for i in range(n):
        for j in range(6):
            if dice[i][j] == num:
                nxt = dice[i][rotate[j]]
                if 6 in [num, nxt]:
                    if 5 in [num, nxt]:
                        result += 4
                    else: result += 5
                else:
                    result += 6
                num = nxt
                break
    return result

for i in range(1, 7):
    ans = max(ans, cal(i))

print(ans)