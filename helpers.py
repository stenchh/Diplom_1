from conftest import db
def get_ingredient_data(db):
    ingredients = db.available_ingredients()
    return [(ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for ingredient in ingredients]


def get_bun_data(db):
    buns = db.available_buns()
    return [(bun.get_name(), bun.get_price()) for bun in buns]

def filtered_ingredient(ingredients, ingredient_type):
    return [ingredient for ingredient in ingredients if ingredient[0] == ingredient_type]