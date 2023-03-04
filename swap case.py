str1=input("enter the string:")
res=''
for i in str1:
    if i.isupper():
        res+=i.lower()
    elif i.islower():
        res+=i.upper()
print(res)
        
