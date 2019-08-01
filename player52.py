a,b=map(int,input().split())
s=list(map(int,input().split()))[:a]
while(b>1):
    d=min(s)
    s.remove(d)
    b=b-1
print(min(s))
