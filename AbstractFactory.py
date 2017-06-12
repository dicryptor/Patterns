import abc

class AbstractFactory(metaclass=abc.ABCMeta):
    """ Declare an interface for operations that create abstract product objects """

    @abc.abstractmethod
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

class ConcreteFactory1(AbstractFactory):
    """ Implement the operations to create concrete product objects """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    """ Implement the operations to create concrete product objects """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(metaclass=abc.ABCMeta):
    """ declare and interface for a type of product """

    @abc.abstractmethod
    def interface_a(self):
        pass

class ConcreteProductA1(AbstractProductA):
    """ define a product object to be created by the corresponding concrete factory """

    def interface_a(self):
        pass

class ConcreteProductA2(AbstractProductA):
    """ define a product object to be created by the corresponding concrete factory """

    def interface_a(self):
        pass

class AbstractProductB(metaclass=abc.ABCMeta):
    """ Declare an interface for a type of product object """

    @abc.abstractmethod
    def interface_b(self):
        pass

class ConcreteProductB1(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete factory.
    Implement the AbstractProduct interface
    """

    def interface_b(self):
        pass

class ConcreteProductB2(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete factory.
    Implement the AbstractProduct interface
    """

    def interface_b(self):
        pass

def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()

if __name__ == "__main__":
    main()


# import random
#
# class PetShop:
#     """ A pet shop"""
#
#     def __init__(self, animal_factory=None):
#         """ pet_factory is the abstract factory, can be set at will"""
#
#         self.pet_factory = animal_factory
#
#     def show_pet(self):
#         """Creates and shows a pet using the abstract factory"""
#
#         pet = self.pet_factory.get_pet()
#         print("We have a lovely {}".format(pet))
#         print("It says {}".format(pet.speak()))
#         print("We also have {}".format(self.pet_factory.get_food()))
#
# # Stuff that our factory makes
# class Dog:
#
#     def speak(self):
#         return "woof"
#
#     def __str__(self):
#         return "Dog"
#
# class Cat:
#
#     def speak(self):
#         return "meow"
#
#     def __str__(self):
#         return "Cat"
#
# # Factory classes
# class DogFactory:
#
#     def get_pet(self):
#         return Dog()
#
#     def get_food(self):
#         return "Dog food"
#
# class CatFactory:
#
#     def get_pet(self):
#         return Cat()
#
#     def get_food(self):
#         return "Cat food"
#
# def get_factory():
#     """ dynamic choice"""
#     return random.choice([DogFactory, CatFactory])()
#
# if __name__ == "__main__":
#     for i in range(15):
#         shop = PetShop(get_factory())
#         shop.show_pet()
#         print("=" * 20)