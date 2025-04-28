import pytest
from helpers import *
from data import BurgerTestingData

class TestDatabase:

    @pytest.mark.parametrize('index_bun, bun_name, bun_price', BurgerTestingData.test_data_buns)
    def test_available_buns(self, index_bun, db, bun_name, bun_price):
        bun_data = get_bun_data(db)
        assert bun_data[index_bun][0] == bun_name
        assert bun_data[index_bun][1] == bun_price

    @pytest.mark.parametrize('index, ingredient_type, ingredient_name, ingredient_price',BurgerTestingData.test_data_ingredients)
    def test_available_ingredients(self, index, db, ingredient_type, ingredient_name, ingredient_price):
        ingredient_data = get_ingredient_data(db)
        assert ingredient_data[index][0] == ingredient_type
        assert ingredient_data[index][1] == ingredient_name
        assert ingredient_data[index][2] == ingredient_price

    def test_get_quantity_available_sauces(self,db):
        ingredient_data = get_ingredient_data(db)
        sauces = filtered_ingredient(ingredient_data, 'SAUCE')
        assert len(sauces) == 3

    def test_get_quantity_of_fillings_exists(self, db):
        ingredient_data = get_ingredient_data(db)
        fillings = filtered_ingredient(ingredient_data, 'FILLING')
        assert len(fillings) == 3