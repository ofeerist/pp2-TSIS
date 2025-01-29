class Higher_mammal():
    def __init__(self):
        self.species = "Higher_mammal"

    def eat(self, food: str):
        print(f"{self.species} ate {food}")

mammal = Higher_mammal()
mammal.eat("Bananas")

class Human():
    def __init__(self, name):
        super().__init__()
        self.species = "Human"
        self.name = name

    def eat(self, food: str):
        print(f"{self.species} named {self.name} ate {food}")

human = Human("Mario")
human.eat("Pasta")

class Student(Human):
    def __init__(self, name, major):
        super().__init__(name)
        self.name = name
        self.major = major

    def eat(self, food: str):
        print(f"{self.species} named {self.name} on major {self.major} ate {food}")

human = Student("Marco", "Math")
human.eat("his own notes")