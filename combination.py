num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

fact1 = 1
fact2 = 1
fact3 = 1

for i in range(1, num1 + 1):
    fact1 *= i

for i in range(1, num2 + 1):
    fact2 *= i

for i in range(1, num1-num2 + 1):
    fact3 *= i

result = (fact1)/((fact2)*(fact3))

print(f"C({num1},{num2}) = {result}")
