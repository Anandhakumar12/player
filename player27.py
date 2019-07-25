ax=input()
az=""
for i in ax:
    if i.isupper():
        b=i.lower()
        az+=b
    elif i.islower():
        c=i.upper()
        az+=c
        
print(az)
