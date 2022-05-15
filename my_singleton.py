class SingletonMeta(type):
    __unique = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__unique:
            instance = super().__call__(*args, **kwargs)
            cls.__unique[cls] = instance
        return cls.__unique[cls]
class Singleton(metaclass=SingletonMeta):
    def do_something(self):
        print('I am created')

a = Singleton()
b = Singleton()
b.do_something()

print(a is b)