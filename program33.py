s=input("enter a string")
if len(s)>2:
    res=s[:2]+s[-2:]
    print(res)
elif len(s)==2:
    res=s+s;
    print(res)
else:
    print(" ")
