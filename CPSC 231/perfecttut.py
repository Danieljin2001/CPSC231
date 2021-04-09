"""
n = int(input("Enter an integer (0 or less to quit): "))
d = n
def function(n,d):
    result = 0
    while d!=0:
        c = n%d
        if c == 0:
            result += d
        d -= 1
    return result
if n<=0:
    exit()
s = function(n,d)
s = s-n
if s == n:
        print("That's a perfect number")
elif s> n:
        print("That's an abundance number")
else:
        print("That's a deficient number")


"""
a = int(input())
b = int(input())
while a <= b:
    if a == 3 or a ==5:
        print ("A")
        a = a+1
    elif a==2:
        print("B")
        a = a+2
    else:
        print(a)
        a = a+1
