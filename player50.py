a=int(input())
k=0
for x in range(2,a):
    if a%x==0:
        k=1
        break
if k==1:
    print("yes")
else:
    print("no")
