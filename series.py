while True:
    print("1.Addition of two numbers ")
    print("2.Subtraction of two numbers")
    print("3.Exit")
    ch=int(input("Enter your choice : "))
    if ch==3:
         break
    elif ch==1:
        a=int(input("Enter a number : "))
        b=int(input("Enter a number : "))
            print("Addition : ", a+b)
        elif ch==2:
            a=int(input("Enter a number : "))
            b=int(input("Enter a number : "))
            print("Diffrence  : ",a-b)
