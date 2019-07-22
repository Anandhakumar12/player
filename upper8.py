a,b=map(str,input().split())
a.lower()
b.lower()
for i in a:
  bc=i.upper()
  break
for x in b:
  c=x.upper()
  break
print(bc+a[1:],c+b[1:])
