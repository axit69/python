# initiate the class
class employee:
    # special method/magic method/dunder method - construactor : these method are immediltely called when object of the class is created. (these method/constructor are use to connect to process, db etc which need to be connected immedialtely after the application is launched)
    def __init__(self):
        print(id(self))
        self.id = 123                   # attributes
        self.salary = 50000
        self.designation = "SDE"
        # print("printing all the attribute")

    def travel(self, destination):
        print(f"employee is now travelling to {destination}")
        print("method is executed")
    

# creating object or instance of the class
sam = employee()
sam.name = "Samuel"             # attributes can be created outside the class well with the help object.
print(sam.name)

# peter = employee()
# print(id(peter))
# sam.travel("mumbai")

# print(type(sam))

# print(sam.salary)

# calling a method
# sam.travel("Mumbai")