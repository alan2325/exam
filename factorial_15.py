a=int(input("Enter a number other than 0 and 1 : "))
def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)
print(f"factorial is : ",fact (a))