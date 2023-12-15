'''write a program to generate all factors of given number'''

def factors(n):
    print('the factors of',n,'are :')
    for i in range(1,n+1):
        if not n%i:
            print(i)
n=int(input('enter a number'))
factors(n)
