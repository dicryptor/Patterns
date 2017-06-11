class Singleton(type):
    """Defined an Instance operation that lets clients access its unique instance"""

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    """Example class"""

    pass

def main():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2

if __name__ == "__main__":
    main()


# class Singleton:
#
#     def __new__(cls):
#
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#
#         return cls.instance
#
# singleton = Singleton()
#
# another_singleton = Singleton()
#
# print(singleton is another_singleton)
#
# singleton.ony