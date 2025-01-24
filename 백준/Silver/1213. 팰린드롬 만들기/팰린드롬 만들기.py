name = input()
keys = sorted(list(set("".join(name))))
dic = {}

odd = []
for key in keys:
    dic[key] = name.count(key)
    
    if name.count(key) % 2:
        odd.append(key)
    
if len(odd) > 1:
    print("I'm Sorry Hansoo")
    
else:
    ans = ''
    for key in keys:
        ans += key * (dic[key] // 2)
    
    if len(odd):
        ans += odd[0] + ans[::-1]
    else:
        ans += ans[::-1]
        
    print(ans)