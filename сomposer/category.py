from interfaces.product_categories import IProductCategory
from dataclasses import dataclass


@dataclass
class CategoryBread(IProductCategory):

    _name = "Категория: Хлеб"
    _products = []

    def add(self, obj):
        self._products.append(obj)

    def remove(self, obj):
        if obj in self._products:
            self._products.remove(obj)

    def create(self):
        print(self.__class__)
        print(f"{self._name}")
        if self._products:
            for product in self._products:
                product.create()


@dataclass
class DairyProducts(IProductCategory):

    _name = "Молочные продукты"
    _products = []

    def add(self, obj):
        self._products.append(obj)

    def remove(self, obj):
        if obj in self._products:
            self._products.remove(obj)

    def create(self):
        print(self.__class__)
        print(f"{self._name}")
        if self._products:
            for product in self._products:
                product.create()


@dataclass
class MeatProducts(IProductCategory):

    _name = "Мясные продукты"
    _products = []

    def add(self, obj):
        self._products.append(obj)

    def remove(self, obj):
        if obj in self._products:
            self._products.remove(obj)

    def create(self):
        print(self.__class__)
        print(f"{self._name}")
        if self._products:
            for product in self._products:
                product.create()
