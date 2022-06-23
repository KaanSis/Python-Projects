#(defining the functions here)
#----------------------------
def add(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)

def multp(num1,num2):
    print(num1*num2)

def div(num1,num2):
    if num1>num2:
        print(num1//num2)
    else:
        print(num2//num1)
#----------------------------

#(Taking the input here)

print("1.ADD","2.SUB","3.MULTP","4.DIV")

#(choosing the operation here)
choice = int(input(("Choose an operation 1/2/3/4:")))

if choice in (1,2,3,4):

    num1 = int(input("enter number1:"))
    num2 = int(input("enter number2:"))

    if choice == 1:
        add(num1,num2)
    elif choice == 2:
        sub(num1,num2)
    elif choice == 3:
        multp(num1,num2)
    elif choice == 4:
        div(num1,num2)
