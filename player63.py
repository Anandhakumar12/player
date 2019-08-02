a=int,input()
s=set(map(int,input().split()))
d=set(map(int,input().split()))

pri=s & d
sd=""
for i in pri:
    sd=sd+str(i),""
    
print(sd)
