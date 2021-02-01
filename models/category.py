from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base
from utils.validators import validate_type, validate_not_empty, validate_len, validate_be_greater_than_zero

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=200), nullable=False)
    description = Column(String(length=500), nullable=False)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        name = validate_len(name, 200, key)
        return name

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        description = validate_not_empty(description, key)
        description = validate_len(description, 500, key)
        return description
