'''reverse of a string using recurssion'''
def rev_string(s):
    if not len(s):
        return ' '
    else:
        return s[-1]+rev_string(s[:-1])
st=input("enter a string")
print(rev_string(st))



'''output
enter a stringfgh
hgf '''
