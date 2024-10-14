n = 3  

for i in range(n):
    if i % 2 == 0:  
        for j in range(n):
            print(chr(65 + j), end=" ")
    else: 
        for j in range(n - 1, -1, -1):
            print(chr(65 + j), end=" ")
    print()