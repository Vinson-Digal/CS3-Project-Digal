class Animal:
    def __init__(self, name, species):
        self.__name = name
        self.species = species

    def make_sound(self):
        pass  

    def eat_food(self):
        pass

    def get_name(self):
        return self.__name
    
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def make_sound(self):
        return " roars loudly!"

    def eat_food(self):
        return " eats fresh meat."

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def make_sound(self):
        return " trumpets!"

    def eat_food(self):
        return " eats grass and fruits."

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, "Monkey")

    def make_sound(self):
        return " chatters!"

    def eat_food(self):
        return " eats bananas."

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.get_name() +"" + lion.make_sound())
print(lion.get_name() +"" + lion.eat_food())
print("-----")
print(elephant.get_name() +"" + elephant.make_sound())
print(elephant.get_name() +"" + elephant.eat_food())
print("-----")
print(monkey.get_name() +"" + monkey.make_sound())
print(monkey.get_name() +"" + monkey.eat_food())
print("-----")