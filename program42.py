'''factorial using recurssion'''

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
m=int(input("enter a no"))
print(fact(m))


'''output
enter a no4
24'''
