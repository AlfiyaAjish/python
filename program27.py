s=input("enter a string")
if s.lower().endswith('ing'):
    s=s+"ly"
else:
    s=s+"ing"
print(s)
    
