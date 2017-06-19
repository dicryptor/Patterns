import abc

class AbstractClass(metaclass=abc.ABCMeta):

    def template_method(self):
        self._step_1()
        self._step_2()
        self._step_3()

    def _step_1(self):
        print("Do standard step 1")

    @abc.abstractmethod
    def _step_2(self):
        print("Do primitive step 2")

    def _step_3(self):
        print("Do standard step 3")

class ConcreteClass(AbstractClass):

    def _step_2(self):
        self._step_2_1()
        self._step_2_2()

    def _step_2_1(self):
        print("Do step 2_1")

    def _step_2_2(self):
        print("Do step 2_2")


def main():
    concrete_class = ConcreteClass()
    concrete_class.template_method()
    # concrete_class.standard_method()

if __name__ == "__main__":
    main()