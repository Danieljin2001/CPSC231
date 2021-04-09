n = input("Enter 2 integers, separated by a space: ")
q = n.split(" ")
p = int(q[0])
m = int(q[1]) 
print(n)
listOfCounters = []
for number in range (p,m+1):
    counter = 1
    while number != 1:
        if number % 2 != 0:
            number=3*number+1
            counter += 1
        else:
            number = number/2
            counter += 1
    listOfCounters.append(counter) #adds to the list
k = max(listOfCounters) #gives biggest integer in list
print(k)
