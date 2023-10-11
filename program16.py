num=input("enter a list of numbers separated with comma")
num=list(map(int,num.split(",")))
print("maximum",max(num))
print("minimum",min(num))
