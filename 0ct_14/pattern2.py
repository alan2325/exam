n = 3  

for i in range(n):
    for j in range(n):
        if i == j:
            print(1, end=" ")
        else:
            print(chr(65 + j), end=" ")
    print()  