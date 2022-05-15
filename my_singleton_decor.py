from dataclasses import dataclass

def singleton(cls):
    unique = {}
    def wrapper(*args, **kwargs):
        if cls not in unique:
            unique[cls] = cls(*args, **kwargs)
        return unique[cls]
    return wrapper

@singleton
class Something:
    def __init__(self, val = 0):
        self._val = val
    @property
    def val(self):
        return self._val
    def viz(self):
        print(7)

def id2val(x):
    import ctypes
    return ctypes.cast(x, ctypes.py_object).value

class File:
    def print(self):
        print(42)

@singleton
@dataclass
class Config(File):
    _file: str = 'pass'


a = Something()
b = Something(5)

print(a.val)
print(b._val)
a.viz()
b.viz()

print(a is b)

n = Config()
m = Config()
n._file = 'lama'
print(n._file)
print(m._file)
k = File()
k.print()
m.print()