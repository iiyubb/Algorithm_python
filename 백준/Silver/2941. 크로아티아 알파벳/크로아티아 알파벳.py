input = input()

ans = 0
while len(input) > 0:

    if 'dz=' in input:
        ans += 1
        input = input.replace("dz=", " ", 1)
        
    elif 'c=' in input:
        ans += 1
        input = input.replace("c=", " ", 1)

    elif 'c-' in input:
        ans += 1
        input = input.replace("c-", " ", 1)
        
    elif 'z=' in input:
        ans += 1
        input = input.replace("z=", " ", 1)

    elif 'd-' in input:
        ans += 1
        input = input.replace("d-", " ", 1)

    elif 'lj' in input:
        ans += 1
        input = input.replace("lj", " ", 1)
        
    elif 'nj' in input:
        ans += 1
        input = input.replace("nj", " ", 1)
        
    elif 's=' in input:
        ans += 1
        input = input.replace("s=", " ", 1)
        
    else:
        input = input.replace(" ", "")
        ans += len(input)
        break
    
print(ans)