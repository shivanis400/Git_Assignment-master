def add(x, y):
   return x + y
def multiply(x, y):
   return x * y
def subs(x,y):
    return x-y
def divison(x,y):
    return x/y 
def calculator():
        print("Select operation.")
        print("1.Add")
        print("2.Multiply")
        print("3.Subtraction")
        print("4.Divison")
        choice = input("Enter choice(1/2/3/4):")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == '1':
                print(num1,"+",num2,"=", add(num1,num2))
        elif choice == '2':
                print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == '3':
                print(num1,"-",num2,"=",subs(num1,num2))
        elif choice == '4':
                print(num1,"/",num2,"=",divison(num1,num2))
        else:
                print("You entered Wrong Input")
print(calculator())
