"""# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")"""



###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################
###################################################################



"""celsius = int(input("Sıcaklığı giriniz: "))

fahrenheit = ((celsius*9 + 160)) / 5

kelvin = celsius + 273

print(f"{celsius} celsius, {fahrenheit} fahrenheit'tır ve {kelvin} kelvin'dir.")"""


###################################################################
###################################################################

"""print("İşlem seçiniz: ")
print("1.gtomg")
print("2.gtokg")
print("3.kgtog")
print("4.kgtomg")
print("5.mgtog")
print("6.mgtokg")

while True:
    
    seçim = input("Seçimi giriniz(1/2/3/4/5/6): ")

    if seçim in('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Ağırlık girin: "))

        if seçim == '1':
            print(f"{num1} gram, {num1 * 1000} miligramdır.")

        elif seçim == '2':
            print(f"{num1} gram, {num1 / 1000} kilogramdır.")

        elif seçim == '3':
            print(f"{num1} kilogram, {num1 * 1000} gramdır.")

        elif seçim == '4':
            print(f"{num1} kilogram, {num1 * 1000000} miligramdır.")
        
        elif seçim == '5':
            print(f"{num1} miligram, {num1 / 1000} gramdır.")

        elif seçim == '6':
            print(f"{num1} miligram, {num1 / 1000000} kilogramdır.")
        break
else:
            print("Geçersiz işlem")"""



sayi = int(input("Değer giriniz: "))

megabayt = sayi

gigabayt = sayi / 1024

terabayt = megabayt / 1048576

print(f"{megabayt} megabayt, {gigabayt} gigabayt ve {terabayt} terabayt'tır.")











