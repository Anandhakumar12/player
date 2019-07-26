a=str(input())
ad=list(a)

pp=""
for i in a:
    ad.remove(i)
    if i not in ad:
        pp+=i
    ad.append(i)
        

print(pp)
        
