F = input("Enter in first name: ")
F += "\n"
L = input("Enter in last name: ")
L += "\n"
S = input("Enter in salary: ")
S += "\n"
first = open("firstName.txt", "w")
first.write(F)
last = open("lastName.txt", "w")
last.write(L)
sal = open("salary.txt", "w")
sal.write(S)
while F != "" and L !="" and S != "":
    F = input("Enter in first name: ")
    L = input("Enter in last name: ")
    S = input("Enter in salary: ") 
    if F !="" and L != "" and S != "":
        first.write(F + "\n")
        last.write(L + "\n")
        sal.write(S + "\n")
first.close()
last.close()
sal.close()

