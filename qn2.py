# 2. Create a calculator that takes two
# numbers and performs addition,
# subtraction, multiplication, and
# division. Ensure all conditions are
# considered.


a = float(input("enter first number"))
b = float(input("enter second number"))

operation = int(input("choose an operation number: 1.addition 2.subtraction 3.multiplication 4.division"))
match operation :
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        if a==0:
            print(a/b)
        else:
            print(b/a)
    case _:
        print("Invalid choice")


        
    
    
