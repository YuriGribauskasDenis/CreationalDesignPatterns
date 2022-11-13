from typing import List

# convert to module, import acquire and release

# context manager
class PoolManager:
    def __init__(self, pool):
        self.pool = pool
    def __enter__(self):
        self.obj = self.pool.aquire()
        return self.obj
    def __exit__(self, type, value, traceback):
        self.pool.release(self.obj)

class Reusable:
    def test(self):
        print(f'reusable object{id(self)}')

class ReusablePool:
    def __init__(self, size):
        self.size = size
        self.free = []
        self.in_use = []
        for _ in range(self.size):
            self.free.append(Reusable())
    def aquire(self) -> Reusable:
        if len(self.free) <= 0:
            raise Exception('no free objects available')
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r
    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)


r0 = Reusable()
r0.test()
print('='*20)

pool = ReusablePool(2)
r = pool.aquire()
r2 = pool.aquire()
r.test()
r2.test()
pool.release(r2)
r3 = pool.aquire()
r.test()
r3.test()
print('='*20)

pool2 = ReusablePool(2)
with PoolManager(pool2) as r:
    r.test()
with PoolManager(pool2) as r:
    r.test()
with PoolManager(pool2) as r:
    r.test()