import sys

input = sys.stdin.readline
bingo = [list(map(int, input().split())) for _ in range(5)]
sel = [list(map(int, input().split())) for _ in range(5)]
speak = sum(sel, [])
ans = [[0] * 5 for _ in range(5)]
cnt = 0
result = 0


def check_row():
    count = 0
    for arr in ans:
        if sum(arr) == 5:
            count += 1
    return count


def check_col():
    count = 0
    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += ans[j][i]
        if tmp == 5:
            count += 1
    return count


def check_dia1():
    count = 0
    # dia1
    tmp1 = 0
    for i in range(5):
        if ans[i][i] == 1:
            tmp1 += 1
    if tmp1 == 5:
        count += 1
    return count


def check_dia2():
    count = 0
    tmp2 = 0
    # dia2
    for i in range(5):
        if ans[i][5 - i - 1] == 1:
            tmp2 += 1
    if tmp2 == 5:
        count += 1
    return count


for i in range(len(speak)):
    result = 0
    for y in range(5):
        for x in range(5):
            if bingo[y][x] == speak[i]:
                ans[y][x] = 1
                cnt += 1

    if cnt >= 12:
        result += check_col()
        result += check_row()
        result += check_dia1()
        result += check_dia2()

        if result >= 3:
            print(i+1)
            break