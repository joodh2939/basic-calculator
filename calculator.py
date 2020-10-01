calculate = True

while calculate:
    try:
        x = int(input("Enter your first number: "))
        y = int(input("Enter your second number: "))

    except(ValueError):
        print("not an integer")

    else:
        o = input("enter your operator in words :")

        if o == "addition" or o == "+":
            a = x + y
            print(f"{x} + {y} = {a}")

        elif o == "subtraction" or o == "-":
            a = x - y
            print(f"{x} - {y} = {a}")

        elif o == "division" or o == "/":
            a = x * y
            print(f"{x} / {y} = {a}")

        elif o == "multiplication" or o == "*":
            a = x * y
            print(f"{x} * {y} = {a}")
        else:
            print("wrong operator")
            print((("""
type addition for addition or "+"
type subtraction for subtraction or "-"
type multiplication for multiplication or "*"
type division for division or "/"
            """)))
        try_again = input("do you want to try again y/n : ")

        if try_again == "yes" or "y":
            calculate = True
        else:
            calculate = False
