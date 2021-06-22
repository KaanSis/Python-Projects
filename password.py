import random

while True:

    lower = "abcdefghijklmnopqrstuvwxyz"

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numbers = "0123456789"

    symbols = "[]{}()*/#&:;.,_-"

    all = lower + upper + numbers + symbols

    userlength = int(input("Password length: "))

    password = "".join(random.sample(all, userlength))

    if userlength > 16:
        print("Enter less digits.")
    elif userlength < 6:
        print("Enter more digits")
    else:
        print(password)
