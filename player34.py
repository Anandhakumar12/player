a=str(input())
ad=""
c=len(a)
dec=0

while c>0:
  
  ad=ad+a[dec]
  dec=dec+3
  c=c-3

print(ad)
