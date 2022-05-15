from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def create(self):
        pass
    def do_smth(self):
        product = self.create()
        product.Salude()

class BuilderShip(Builder):
    def create(self):
        return EntityShip()

class BuilderTruck(Builder):
    def create(self):
        return EntityTruck()

class Entity(ABC):
    @abstractmethod
    def Salude(self):
        pass

class EntityShip(Entity):
    def Salude(self):
        print('tuh-tuh')

class EntityTruck(Entity):
    def Salude(self):
        print('bru-bru')

def client_code(builder):
    builder.do_smth()

if __name__ == "__main__":
    client_code(BuilderShip())
    client_code(BuilderTruck())