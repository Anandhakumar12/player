a,b=map(int,input().split())
key=0
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        key=i
        break
    
print(key)
