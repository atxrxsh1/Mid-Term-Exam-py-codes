a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if a>b and b>c :
    if b>c:
        print(a,b,c,sep='>')
    else:
        print(a,c,b,sep=">")
elif b>a and b>c:
    if a>c:
        print(b,a,c,sep=">")
    else:
        print(b,c,a,sep=">")
elif c>a and c>b:
    if a>b:
        print(c,a,b,sep=">")
    else:
        print(c,b,a,sep=">")