n = 65 

for i in range(3):
    a=1
    for j in range(3):
        if i == j:
            print(a, end=" ")
        else:
            print(chr(n), end=" ")
    print()
    n+=1


   

    ##1 A A
    ##B 1 B 
    ##C C 1