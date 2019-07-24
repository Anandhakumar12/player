s = input()
dic1 = {}
for c1 in s :
    if c1 in dic1 :
        dic1[c1] += 1
    else :
        dic1[c1] = 1
foo = 0
for x in dic1 :
    if dic1[x] > f :
        foo = dic1[x]
        key = x
print(key)
print(dic1)
