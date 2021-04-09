f = input("enter number: ")
g = input("enter in number to divide the first number by: ")

while f != "" and g != "":
    try:
        p = int(f)/int(g)
        print(f"{f} divided by {g} = {p}")
        f = input("enter number: ")
        g = input("enter in number to divide the first number by: ")
    except ValueError as value_error:
        print(f"ValueError: input(s) were not an integer")
        f = input("enter number: ")
        g = input("enter in number to divide the first number by: ")
    except ZeroDivisionError as dividedbyzero:
        print("ZeroDivionError, Can't divide by zero")
        f = input("enter number: ")
        g = input("enter in number to divide the first number by: ")
    except:
        print("Something else went wrong")
        f = input("enter number: ")
        g = input("enter in number to divide the first number by: ")
exit()               
              

