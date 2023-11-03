'''increment a list of integers by 10% if the number is greater than 1000 else by 5%'''

a=map(int,input("enter a number").split())
l=list(map(lambda x:x+x*0.1 if x>1000 else x+x*0.05,a))
print(l)
