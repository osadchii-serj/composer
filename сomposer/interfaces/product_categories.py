from abc import ABC, abstractmethod


class IProductCategory(ABC):

    _name = None

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass
