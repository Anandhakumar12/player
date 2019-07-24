aa,bb = map(int,input().split())
for imax in range(max(aa,bb), aa*bb+1) :
    if (imax%aa == 0) and (imax%bb == 0) :
        ans = imax
        break
print(ans)
