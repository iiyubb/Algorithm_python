x, y = map(int, input().split())
n = int(input())
locs = [list(map(int, input().split())) for _ in range(n)]
dong = list(map(int, input().split()))

def cal(p, dist):
    if p == 1:
        return dist
    elif p == 2:
        return x + y + x - dist
    elif p == 3:
        return 2*x + y + y - dist
    elif p == 4:
        return x + dist

ans = 0
dong_path = cal(dong[0], dong[1])
for loc in locs:
    loc_path = cal(loc[0], loc[1])
    dist = abs(dong_path - loc_path)
    ans += min(dist, 2*x + 2*y - dist)

print(ans)

