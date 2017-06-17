import abc

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def algorithm_interface(self):
        pass


class ConcreteStrategyA(Strategy):

    def algorithm_interface(self):
        print("Strategy A used")

class ConcreteStrategyB(Strategy):

    def algorithm_interface(self):
        print("Strategy B used")

def main():
    concrete_strategy_a = ConcreteStrategyA()
    concrete_strategy_b = ConcreteStrategyB()

    context = Context(concrete_strategy_a)
    context.context_interface()

    context = Context(concrete_strategy_b)
    context.context_interface()


if __name__ == "__main__":
    main()