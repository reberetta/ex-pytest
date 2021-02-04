import sys

sys.path.append('.')
import pytest
from controllers.category_controller import CategoryController
from controllers.base_controller import BaseController
from models.category import Category

class TestCategoryController:
    @pytest.fixture
    def create_instance(self):
        controller_category = CategoryController()
        return controller_category
    
    def test_category_controller_instance(self, create_instance):
        assert isinstance(create_instance, BaseController)
        assert isinstance(create_instance, CategoryController)
    
    def test_category_read_all_return(self, create_instance):
        list_ = create_instance.read_all()
        assert isinstance(list_, list)
    
    def test_category_create(self, create_instance):
        category = Category('celulares', 'descrição valida')
        obj = create_instance.save(category)
        assert not obj.id_ is None
        assert obj.name == 'celulares'
        assert obj.description == 'descrição valida'
        create_instance.delete(obj)
    
    def test_category_create_not_valid_model(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.save('s')

    def test_category_read_by_id_return(self, create_instance):
        category = Category('nome valido', 'descricao valida')
        created = create_instance.save(category)
        obj = create_instance.read_by_id(created.id_)
        assert isinstance(obj, Category)
        assert obj.name == 'nome valido'
        assert obj.description == 'descricao valida'
        create_instance.delete(obj)
    
    def test_category_read_by_id_with_invalid_id(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.read_by_id('a')

    def test_update_category(self, create_instance):
        category = Category('name', 'description')
        obj = create_instance.save(category)
        obj.name = 'a'
        obj.description = 'b'
        id_ = create_instance.save(obj)
        id_ = id_.id_
        object_ = create_instance.read_by_id(id_)
        assert object_.name == 'a'
        assert object_.description == 'b'
        assert isinstance(object_, Category)
        create_instance.delete(object_)
    
    def test_delete_not_valid_model(self, create_instance):
    with pytest.raises(TypeError):
        create_instance.delete('a')