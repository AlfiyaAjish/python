'''sum of n whole number'''
def whole(n):
    if not n:
        return 0
    else:
        return n+whole(n-1)
m=int(input("enter a no"))
print(whole(m-1))
'''output
enter a no5
10'''
