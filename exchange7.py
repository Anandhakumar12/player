av="abcd"
h=[]
g=[]
gh=[]
hg=[]
jkh=""
for i in av:
  if av.index(i)%2==0:
    h.append(i)
  else:
    g.append(i)
we=list(zip(g,h))

for ii in we:
    gh.append(list(ii))

for re in gh:
    for er in re:
        hg.append(er)
        
pr=(''.join(hg))
print(pr)

