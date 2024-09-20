from interfaces.product_categories import IProductCategory
from dataclasses import dataclass


@dataclass
class Bread(IProductCategory):

    _name = "Продукт: Белый хлеб"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class WholeGrainBread(IProductCategory):

    _name = "Продукт: Цельнозерновой хлеб"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class Ciabatta(IProductCategory):

    _name = "Продукт: Чиабатта"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class Milk(IProductCategory):

    _name = "Продукт: Молоко"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class Yogurt(IProductCategory):

    _name = "Продукт: Йогурт"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class SalamiMilanese(IProductCategory):

    _name = "Продукт: Салями Миланская"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class Bacon(IProductCategory):

    _name = "Продукт: Бекон"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class BoiledSausage(IProductCategory):

    _name = "Продукт: Колбаса вареная"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class GroundMeat(IProductCategory):

    _name = "Продукт: Фарш мясной"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()


@dataclass
class SmokedSausage(IProductCategory):

    _name = "Продукт: Копченая колбаса"
    _compound_list = []

    def add(self, obj):
        self._compound_list.append(obj)

    def remove(self, obj):
        if obj in self._compound_list:
            self._compound_list.remove(obj)

    def create(self):
        print(f"\t{self.__class__}")
        print(f"\t{self._name}")
        if self._compound_list:
            for product in self._compound_list:
                product.create()
