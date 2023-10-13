s=input("enter a wprd")
letter={}
for i in s:
    letter[i]=letter.get(i,0)+1
print(letter)
