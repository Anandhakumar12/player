a=int(input())
li=str(input())
lis=['a','e','i','o','u','A','E','I','O','U']
asd=""
for i in li:
    if i not in lis:
        asd=asd+i
        
print(asd[::-1])
