'''Accept a list of integers from user. For all values above 100 store the string 'Over' in the specific position.'''

def over(l):
    for i in range(len(l)):
        if l[i]>100:
            l[i]='over'
    return l
        
        

l=list(map(int,input('enter a list of num with space').split()))
print(over(l))
