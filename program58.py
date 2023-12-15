try:
    x=int(input("enter a number"))
    if x<90 or x>120:
        raise ValueError
    else:
        print(x)
except ValueError:
    print("abnormal condition")
finally:
    print("i am done")
