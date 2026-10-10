class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def sound(self):
            print("Animal sound")
    def move(self):
            print("Animal move")
class Cow(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
        
animal1 = Animal('Dog', 'yellow')
animal2 = Animal('Cat', 'white')
animal2 = Cow('cow', 'black')

print(animal1.name)
print(animal1.color)
print(animal2.name)
print(animal2.color)

animal1.sound()
animal1.move()
animal2.sound()
animal2.move()