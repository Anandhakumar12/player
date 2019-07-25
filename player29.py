a,b=map(int,input().split())
key=0
for i in range(1,max(a,b)+1):
  o=i*i
  if o>=min(a,b) and o<=max(a,b):
    key=key+1

print(key)
