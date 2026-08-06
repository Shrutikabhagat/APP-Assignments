class Apple:
    def display(self):
        print("Fruit: Apple")


class Mango:
    def display(self):
        print("Fruit: Mango")


class Orange:
    def display(self):
        print("Fruit: Orange")


class FruitFactory:
    @staticmethod
    def get_fruit(fruit_name):
        if fruit_name.lower() == "apple":
            return Apple()
        elif fruit_name.lower() == "mango":
            return Mango()
        elif fruit_name.lower() == "orange":
            return Orange()
        else:
            return None


# Using the factory
f1 = FruitFactory.get_fruit("Apple")
f2 = FruitFactory.get_fruit("Mango")
f3 = FruitFactory.get_fruit("Orange")

f1.display()
f2.display()
f3.display()