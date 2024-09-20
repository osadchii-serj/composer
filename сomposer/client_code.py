from interfaces.product_categories import IProductCategory

from ingredients import IngredientsWholeGrainBread
from ingredients import IngredientsSmokedSausage
from ingredients import IngredientsSalamiMilanese
from ingredients import IngredientsBoiledSausage
from ingredients import IngredientsGroundMeat
from ingredients import IngredientsWhiteBread
from ingredients import IngredientsCiabatta
from ingredients import IngredientsYogurt
from ingredients import IngredientsBacon
from ingredients import IngredientsMilk

from products import WholeGrainBread
from products import SmokedSausage
from products import SalamiMilanese
from products import BoiledSausage
from products import GroundMeat
from products import Ciabatta
from products import Yogurt
from products import Bread
from products import Bacon
from products import Milk

from category import CategoryBread
from category import DairyProducts
from category import MeatProducts


def client_code(
    category: IProductCategory, product: IProductCategory, ingredient: IProductCategory
):
    category.add(product)
    product.add(ingredient)
    category.create()


if __name__ == "__main__":
    print("===" * 35)
    client_code(CategoryBread(), Bread(), IngredientsWhiteBread())
    print("===" * 35)
    client_code(CategoryBread(), WholeGrainBread(), IngredientsWholeGrainBread())
    print("===" * 35)
    client_code(CategoryBread(), Ciabatta(), IngredientsCiabatta())
    print("===" * 35)
    client_code(DairyProducts(), Milk(), IngredientsMilk())
    print("===" * 35)
    client_code(DairyProducts(), Yogurt(), IngredientsYogurt())
    print("===" * 35)
    client_code(MeatProducts(), SalamiMilanese(), IngredientsSalamiMilanese())
    print("===" * 35)
    client_code(MeatProducts(), Bacon(), IngredientsBacon())
    print("===" * 35)
    client_code(MeatProducts(), BoiledSausage(), IngredientsBoiledSausage())
    print("===" * 35)
    client_code(MeatProducts(), GroundMeat(), IngredientsGroundMeat())
    print("===" * 35)
    client_code(MeatProducts(), SmokedSausage(), IngredientsSmokedSausage())
    print("===" * 35)
