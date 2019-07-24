aa,bb = map(int,input().split())
for imax in range(max(a,b), a*b+1) :
    if (i%aa == 0) and (i%bb == 0) :
        ans = imax
        break
print(ans)
