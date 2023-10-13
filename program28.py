s=input("eneter string").split()
s.sort(key=len,reverse=True)
print("length of the longest word is:",len(s[0]))
if (len(s[0])==len(s[1])):
    print("bingo")
