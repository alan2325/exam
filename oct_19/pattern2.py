a=65
for i in range(3,0,-1):
    for j in range(i):
        print(chr(a+j),end="\t"),
    print()