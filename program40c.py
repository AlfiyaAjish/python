big_string=lambda s:[x for x in s.split() if len(x)>5]
a=input("enter collection of strings")
print(big_string(a))


'''output
enter collection of stringsanu manu ranju alfiya basid 
['alfiya']'''
