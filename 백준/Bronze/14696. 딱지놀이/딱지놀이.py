n = int(input())

for i in range(n):
    a_tmp = input().split()
    a_have = list(map(int, a_tmp[1:]))
    b_tmp = input().split()
    b_have = list(map(int, b_tmp[1:]))

    if a_have.count(4) > b_have.count(4):
        print("A")
    elif a_have.count(4) < b_have.count(4):
        print("B")
    else:
        if a_have.count(3) > b_have.count(3):
            print("A")
        elif a_have.count(3) < b_have.count(3):
            print("B")
        else:
            if a_have.count(2) > b_have.count(2):
                print("A")
            elif a_have.count(2) < b_have.count(2):
                print("B")
            else:
                if a_have.count(1) > b_have.count(1):
                    print("A")
                elif a_have.count(1) < b_have.count(1):
                    print("B")
                else:
                    print("D")