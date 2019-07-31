a=int(input())
ad=""
for i in range(1,a+1):
  if a%i==0 and i%2!=0:
    ad=ad+str(i)+" "
    
print(ad)
