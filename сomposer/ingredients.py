from interfaces.product_categories import IProductCategory
from dataclasses import dataclass


@dataclass
class IngredientsWhiteBread(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tмука пшеничная 1 сорта",
        "\t\t\t\tмука ржаная обдирная",
        "\t\t\t\tдрожжи",
        "\t\t\t\tсолод",
        "\t\t\t\tвода",
        "\t\t\t\tсоль",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsWholeGrainBread(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tмука пшеничная 1 сорта",
        "\t\t\t\tмука ржаная обдирная",
        "\t\t\t\tмука цельнозерновая",
        "\t\t\t\tмасло подсолнечное",
        "\t\t\t\tэкстракт солодовый",
        "\t\t\t\tхлопья ржаные",
        "\t\t\t\tдрожжи",
        "\t\t\t\tсахар",
        "\t\t\t\tвода",
        "\t\t\t\tсоль",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsCiabatta(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tовощные или пряные добавки",
        "\t\t\t\tспеции",
        "\t\t\t\tмука",
        "\t\t\t\tдрожжи",
        "\t\t\t\tвода",
        "\t\t\t\tсоль",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsMilk(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tлактоза",
        "\t\t\t\tбелок",
        "\t\t\t\tвода",
        "\t\t\t\tзола",
        "\t\t\t\tжир",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsYogurt(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tмолоко обезжиренное",
        "\t\t\t\tуглеводы",
        "\t\t\t\tзакваска",
        "\t\t\t\tпектин",
        "\t\t\t\tбелки",
        "\t\t\t\tжиры",
        "\t\t\t\tвода",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsSalamiMilanese(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tантиокислитель(аскорбиновая кислота)",
        "\t\t\t\tусилитель вкуса и аромата (Е621)",
        "\t\t\t\tгрудинка свиная",
        "\t\t\t\tпряности",
        "\t\t\t\tгорчица",
        "\t\t\t\tчеснок",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsBacon(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tбелки",
        "\t\t\t\tжиры",
        "\t\t\t\tвода",
        "\t\t\t\tзола",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsBoiledSausage(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tмясо свинины и говядины",
        "\t\t\t\tспеции (перец, чеснок)",
        "\t\t\t\tшпик",
        "\t\t\t\tсоль",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsGroundMeat(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tмясо свинины и говядины (или курицы)",
        "\t\t\t\tспеции (перец, чеснок)",
        "\t\t\t\tсоль",
        "\t\t\t\tлук",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)


@dataclass
class IngredientsSmokedSausage(IProductCategory):

    _name = "Состав:"
    _compound = [
        "\t\t\t\tмясо свинины и говядины",
        "\t\t\t\tспеции (перец, кориандр)",
        "\t\t\t\tдымный ароматизатор",
        "\t\t\t\tшпик",
        "\t\t\t\tсоль",
    ]

    def add(self, obj):
        return super().add(obj)

    def remove(self, obj):
        return super().remove(obj)

    def create(self):
        print(f"\t\t\t{self.__class__}")
        print(f"\t\t\t{self._name}")
        for product in self._compound:
            print(product)
