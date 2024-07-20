L=[1,2,3,4,4,3]
new=[]
for i in L:
    if i not in new:
        new.append(i)
print(new)