from dao.base_dao import BaseDao
from models.base_model import BaseModel


class BaseController:
    def __init__(self, dao: BaseModel) -> None:
        self.__dao = dao
    
    def save(self, model: BaseModel) -> BaseModel:
        return self.__dao.save(model)
    
    def read_all(self) -> list:
        return self.__dao.read_all()
    
    def read_by_id(self, id_: int) -> BaseModel:
        return self.__dao.read_by_id(id_)
    
    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
