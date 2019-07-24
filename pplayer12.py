l,m=map(int,input().split())
l1=list(map(int,input().split()))
lo=""
l2=l1[0:m+1]
l23=l1[m+1:]


pr=(l23+l2)
for i in pr:
    lo=lo+str(i)+" "
    
print(lo)
