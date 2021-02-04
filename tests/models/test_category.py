import sys

sys.path.append('.')
import pytest

from models.category import Category


class TestCategoryModel:
    @pytest.mark.parametrize("name, description", [
        ('Nada', ''),
        ('', 'fgssrhyrshyrs'),
        (None, 'fasfafaf'),
        ('fasfafaf', None),
        ('N' * 220, 'D' * 255),
        ('N' * 120, 'D' * 520),
        (10, 'teste'),
        ('fsfsdf',15)
    ])
    def test_empty_name(self, name, description):
        with pytest.raises(ValueError):
            cat = Category(name, description)


    @pytest.mark.parametrize("name, description", [
        ('Nada', '52352323'),
        ('42342', 'fgssrhyrshyrs'),
        ('None', 'fasfafaf'),
        ('fasfafaf', 'None'),
        ('N' * 20, 'D' * 55),
        ('N' * 20, 'D' * 20)
    ])
    def test_Category(self, name, description):
        Category(name, description)


    @pytest.mark.parametrize("name, description", [
        (10, 'teste'),
        ('fsfsdf',15)
    ])
    def test_empty_name(self, name, description):
        with pytest.raises(TypeError):
            cat = Category(name, description)