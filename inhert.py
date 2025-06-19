class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}, makes a sound. ")
        # animal.type("crow")


class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.behaviour = "friendly"
        


    def speak(self):
        # print(f"{self.name}, barks")
        super().speak()
        print(f"{self.name} is {self.behaviour}")

        
animal = Animal("tommy")
# animal.speak()

dog1 = Dog()




 
