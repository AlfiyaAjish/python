num=input("enter a list of numbers separated with comma")
num=list(map(int,num.split(",")))
result=[i for i in num if (i%2==0) and i>0]
print(result)

