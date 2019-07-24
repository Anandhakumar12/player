s = input()
dic1 = {}
for c1 in s :
    if c1 in dic1 :
        dic1[c1] += 1
    else :
        dic1[c1] = 1

fool = 1
for x in dic1 :
    if dic1[x] == fool :
        foo = dic1[x]
        keys = x
print(keys)
