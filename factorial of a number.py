n=int(input("Enter a number : "))
s=1
print(n,"!:",end="")
for i in range (n,0,-1):
    if i>1:
        print(i,end="*")
    else:
        print(i,end="=")
    s=s*i
print(s)