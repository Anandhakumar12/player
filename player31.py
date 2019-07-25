a=str(input())
c=0
d=0
for i in a:
    if i=='(':
        c=c+1
    elif i==')':
        d=d+1
        
if c==d:
    print('yes')
else:
    print('no')
