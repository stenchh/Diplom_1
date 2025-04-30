from praktikum.bun import Bun
import pytest

class TestBunModel:
    def test_bun_has_valid_name(self):
        bun = Bun(name="Ordinary Bun", price=0.5)
        assert bun.name == "Ordinary Bun"

    def test_bun_has_valid_price(self):
        bun = Bun(name="Ordinary Bun", price=0.5)
        assert bun.price == 0.5




