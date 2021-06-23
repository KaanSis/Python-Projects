def perm(x, y):

    factorial1 = 1
    factorial2 = 1

    for i in range(1, x + 1):
        factorial1 *= i

    for i in range(1, x - y + 1):
        factorial2 *= i

    result = (factorial1) / (factorial2)
    print(f"P({x},{y}) = {result}")

#(5 and 3 here is an example, you can enter any number here you want.)
perm(5, 3)

#The result
P(5,3) = 60.0
