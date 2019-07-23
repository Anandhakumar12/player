a=str(input())
lis=['a','e','i','o','u','A','E','I','O','U']
asd=""
for i in a:
    if i not in lis:
        asd=asd+i
        
print(asd[::-1])
