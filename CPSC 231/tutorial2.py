"""
userPass = input("Enter in a password: ")

trialPass = input("Enter in the password again: ")


counter = 0
if trialPass == userPass:
    print("success!")
while (trialPass != userPass) and (counter < 3):
    trialPass = input("try to enter in the password again: ")
    counter = counter + 1
    if trialPass == userPass:
        print("nice")
exit()

"""
inp_1 = "Sp152,g256"
inp_2 = ","
inp_3 = "1gS"

len3 = len(inp_3) - 1
A = list(inp_3)
while len3 >= 0:
    B = A[len3]
    inp_1 = inp_1.replace(B,"")
    len3 -= 1
C = inp_1.split(inp_2)
print(C)
    
