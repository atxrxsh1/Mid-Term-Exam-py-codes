#for increasing order
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print()


print()


# for decreasing order
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print()