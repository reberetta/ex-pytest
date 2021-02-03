from controllers.base_controller import BaseController
from dao.category_dao import CategoryDao


class CategoryController(BaseController):
    def __init__(self):
        super().__init__(CategoryDao())
