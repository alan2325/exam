import cal
while True:
    def main():
        a=int(input("Enter a number : "))
        b=int(input("Enter another number : "))


        ch=int (input("enter choice \n1.add \n2.sub \n3.nul \n4.div \n5mod \n 6.exit"))

    
        if ch == 1:
            print("sum is :", cal.add(a,b))
        elif ch == 2:
            print("sub is :", cal.subtract(a,b))
        elif ch == 3:
            print("Mul is :", cal.multiply(a,b))
        elif ch == 4:
            print("div is :", cal.divide(a,b))
        elif ch == 5 :
            print("mod is : ",cal.mod(a,b))
        elif ch == 6:
            print("You have exited ")
        else:
            print("Invalid input")

    if __name__ == "_main_":
        main()




