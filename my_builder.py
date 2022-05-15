from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass
    @abstractmethod
    def add_base(self):
        pass
    @abstractmethod
    def add_era(self):
        pass
    @abstractmethod
    def add_turret(self):
        pass

class VehBuilder(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self.__product = APC()
    @property
    def product(self):
        product = self.__product
        self.reset()
        return product
    def add_base(self):
        self.__product.add_part('Base')
    def add_era(self):
        self.__product.add_part('ERA')
    def add_turret(self):
        self.__product.add_part('Turret')
    

class InstrBuilder(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self.__product = APC()
    @property
    def product(self):
        product = self.__product
        self.reset()
        return product
    def add_base(self):
        self.__product.add_part('page about Base')
    def add_era(self):
        self.__product.add_part('page about ERA')
    def add_turret(self):
        self.__product.add_part('page about Turret')

class APC:
    TYPE = 'Fighting Vehicle'
    def __init__(self):
        self.__parts = []
    def add_part(self, part):
        self.parts.append(part)
    @property
    def parts(self):
        return self.__parts

class ManualToAPC:
    TYPE = 'APC Manual'
    def __init__(self):
        self.__parts = []
    def add_part(self, part):
        self.parts.append(part)
    @property
    def parts(self):
        return self.__parts

class Director:
    def __init__(self):
        self.__builder = None
    @property
    def builder(self):
        return self.__builder
    @builder.setter
    def builder(self, builder):
        self.__builder = builder
    def build_transport(self):
        self.builder.add_base()
    def build_pioneer(self):
        self.builder.add_base()
        self.builder.add_turret()
    def build_outposter(self):
        self.builder.add_base()
        self.builder.add_turret()
        self.builder.add_era()

if __name__ == "__main__":
    director = Director()
    veh_builder = VehBuilder()
    instr_builder = InstrBuilder()

    director.builder = veh_builder
    director.build_pioneer()
    print(veh_builder.product.parts)
    director.build_outposter()
    print(veh_builder.product.parts)

    director.builder = instr_builder
    director.build_outposter()
    print(instr_builder.product.parts)