'''recursion func for sum'''
def sum(seq):
    if len(seq)==1:
        return (seq[0])
    else:
        return (seq[0]+sum(seq[1:]))
l=[1,2,3,4,5]
print(sum(l))
