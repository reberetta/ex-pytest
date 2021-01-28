from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import validates

class Category():
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=200), nullable=False)
    description = Column(String(length=500), nullable=False)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")
        if not name:
            raise ValueError('Name should not be empty!')
        if len(name) > 200:
            raise ValueError('Name should be 200 chars or less!')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description should be a string')
        if not description:
            raise ValueError('Description should not be empty!')
        if len(description) > 500:
            raise ValueError('Description should be 500 chars or less!')
        return description
