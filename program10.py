l=input("enter colors seperated with comma")
l=l.split(",")
res=[l[i] for i in range (len(l)) if i%2!=0]
print("the original list",l)
print("alternate colors from the list",res)
