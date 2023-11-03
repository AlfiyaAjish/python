'''sum og degits using recurssion'''
 sumdeg(n):
    if not (n/10):
        return n
    else:
        return(n%10)+sumdeg(n//10)
print(sumdeg(1234))


'''output
10'''
