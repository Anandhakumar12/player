a,b=map(str,input().split())
bd=int(b)
if bd%len(a)==0:
  print(a)
elif bd%len(a)!=0:
  bc=bd%len(a)
  print(a[-bc:]+a[:-bc])
