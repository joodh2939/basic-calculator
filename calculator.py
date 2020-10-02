calculate = True

while calculate:
    try:
        x = int(input("enter your first number :"))
        y = int(input("enter your secound number :"))

    except(ValueError):
        print("not an integer")

    else:
        o = input("enter your operator in words :")

        if o == "addition":
            a = x + y
            print(f"{x} + {y} = {a}")

        elif o == "subtraction":
            a = x - y
            print(f"{x} - {y} = {a}")

        elif o == "division":
            a = x * y
            print(f"{x} / {y} = {a}")

        elif o == "multiplication":
            a = x * y
            print(f"{x} * {y} = {a}")
        elif o == "greater than":
            if x > y:
                print("x is greater than y")
            elif x < y:
                print("x is smaller than y")
        elif o == "smaller than":
            if x < y:
                print("x is smaller than y")
            elif x > y:
                print("x is greater than y")

        else:
            print("wrong operator")
            print((("""
            type addition for addition
            type subtraction for subtraction
            type multiplication for multiplication
            type division for division
            type greater than for checking which is greater
            type smaller than for checking which is smaller
                        """)))
            try_again = input("do you want to try again yes/no : ")

            if try_again == "yes":
                calculate = True
            else:
                calculate = False



