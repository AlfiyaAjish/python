n=int(input("enter future year"))
leap=[i for i in range(2023,n) if i%4==0 and (i%400==0 or i%100!=0)]
print(leap)
