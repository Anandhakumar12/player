a=int(input())
s=list(map(int,input().split()))[:a]
d=min(s)
s.remove(d)
print(min(s))
