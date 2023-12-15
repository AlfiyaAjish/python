'''write a program to tdemostrate assertion error in python for negative numbe'''
try:
    x=int(input("enter a number"))
    assert(x>0),'too low value'
except AssertionError as ae:
    print(ae)  
finally:
    print("iam done")
