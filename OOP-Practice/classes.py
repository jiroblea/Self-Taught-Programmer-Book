# Inheritance

class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def name(self):
        """Return name"""
        return self.name

    def age(self):
        """Return age"""
        return self.age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def talk(self, phrase):
        """Phrases after 'Hello!'"""
        print("Hello! {}".format(phrase))

    def walk(self, distance):
        """distance in kilometers"""
        print("I walked {} kilometers.".format(distance))

class Adult(Person):    
    def drive(self, car_brand):
        print("{} is driving their {}.".format(self.name, car_brand))

    def drink_alcohol(self, alcohol_brand):
        return alcohol_brand


def main():
    tom  = Person("Tom", 6)
    tom.print_name()
    tom.print_age()
    tom.talk("How are you?")

    sam = Person("Sam", 7)
    sam.print_name()
    sam.print_age()

    becky = Adult("Becky", 34)
    print("I am {}, {} years of age.".format(becky.name, becky.age))
    becky.talk("I drive a lot!")
    becky.drive("Volkswagen")
    print("I can drink {}.".format(becky.drink_alcohol("rum")))

    sara = Person("Sara", 27)
    print(f"I am {sara.name}, {sara.age} years of age.")
    sara.talk("I walked a lot!")
    sara.walk(7)


if __name__ == "__main__":
    main()
