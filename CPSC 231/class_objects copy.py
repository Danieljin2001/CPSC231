class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
p2 = Person("Amy", 12)
p2.myfunc()
print(p1.age)
del p1.age
try:
    print(p1.age)
except:
    print("no age")
