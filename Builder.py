import abc

class Director:
    """
    construct an object using the Builder interface
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()

class Builder(metaclass=abc.ABCMeta):
    """
    specify an abstract interface for creating parts of a product object
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass

class ConcreteBuilder(Builder):
    """
    construct and assemble parts of the product by implementing the Builder interface
    Define and keep track of the representation it creates.
    provide an interface for retrieving the product
    """

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        self


class Product:
    """
    represent the complex object under construction
    """

    pass

def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product

if __name__ == "__main__":
    main()