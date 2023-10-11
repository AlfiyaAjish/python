n=int(input("enter the no of names"))
names=[]
for i in range (n):
      name=input("enter the names")
      names.append(name)
letter="a"
result=[i for i in names if i[0].lower()==letter]
print(len(result))
       
