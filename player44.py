a=str(input())
b=int(input())
if b%len(a)==0:
  print(a)
elif b%len(a)!=0:
  bc=b%len(a)
  print(a[-bc:]+a[:-bc])
