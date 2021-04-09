DN = int(input("type in decimal number: "))
r = ""
while DN >0:
    remainder = DN%2
    DN = DN//2
    print(str(remainder))
if DN == 0:
    print("0")
