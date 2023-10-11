n=int(input("enter the limit of numbers"))
a=[]
for i in range(n):
    num=int(input("enter the number"))
    a.append(num)
print("strongest neighbour of",a[0],"= ",a[1])
for i in range(1,n-1):
    if a[i-1]>a[i+1]:
         print("Strongest neighbour of",a[i],"= ",a[i-1])
    else:
        print("Strongest neighbour of",a[i],"= ",a[i+1])
print("Strongest neighbour of",a[n-1],"= ",a[n-2])
            
