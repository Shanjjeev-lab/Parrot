class Parrot:
    species = "Bird"

    def __init__(self,name,age):
        
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} is a {self.species} and its age is {self.age}")

polly = Parrot("Polly", 5)
polly.display()

george = Parrot("George", 4)
george.display()
