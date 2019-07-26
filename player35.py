import re
a=str(input())
ad=list(a)

pp=""
for i in a:
    ad.remove(i)
    if i not in ad:
        pp+=i+" "
    ad.append(i)
        

we=re.sub(' +',' ',pp)
print(we)
        

