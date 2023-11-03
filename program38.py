def even(l):
    for item in l:
        if(item==237):
            break
        elif not item%2:
            print(item)
n=input("enter collection of integers")
n=list(map(int,n.split()))
even(n)


'''output'''
'''enter collection of integers2 4 5 238 237 10 12 
2
4
238'''
