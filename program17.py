list=input("enter the elemnts separated with comma")
list=list.split(",")
list2=[]
for item in list:
    if (item not in list2):
        list2.append(item)
print(list2)        
