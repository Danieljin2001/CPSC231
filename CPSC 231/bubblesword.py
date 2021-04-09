"""
a = [10,2,1,7,6]

def replace(numbers,x,y):
    tempy = numbers[y]
    tempx = numbers[x]
    numbers[y] = numbers[x]
    numbers[x] = tempy
i = 0
while i < len(a)-1:
    if a[i] > a[i+1]:
        replace(a,i,i+1)
    print(a)    
    i = i + 1
print(a)
"""
ls = [10,2,1,7,6]
def swap(values,i,j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def bubble(values):
    condition = True
    while condition == True:
        condition = False
        i=0
        while i < len(values)-1:
            if values[i] > values[i+1]:
                swap(values, i , i+1)
                condition = True
            i = i+1
        return values
print(bubble(ls))
