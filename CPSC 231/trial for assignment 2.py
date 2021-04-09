class Student:
    firstname = "f"
    def info(self, name):
        self.firstname += name
        print(self.firstname)
    print("first")
a = input("Add a name: ")
b = input("Add a name: ")

one = Student()
two = Student()

one.info(a)
two.info(b)




