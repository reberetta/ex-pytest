import sys
sys.path.append('.')

from models.category import Category

name = 'Smartphone'
description = 'Uma descrição de categoria'

def test_instance():
    cat = Category(name, description)
    assert isinstance(cat, Category)

def test_empty_name():
    try:
        cat = Category('', description)
        raise NotImplementedError('Exception not raised!')
    except Exception as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

def test_none_name():
    try:
        cat = Category(None, description)
        raise NotImplementedError('Exception not raised!')
    except Exception as error:
        assert isinstance(error, TypeError), 'Invalid Exception!'

def test_name_nostring():
    try:
        cat = Category(10, description)
        raise NotImplementedError('Exception not raised!')
    except Exception as error:
        assert isinstance(error, TypeError), 'Invalid Exception!'


def test_name_lenght():
    try:
        cat = Category('*' * 201, description)
        raise NotImplementedError('Exception not raised!')
    except ValueError as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

def test_description_lenght():
    try:
        cat = Category(name, '*' * 501)
        raise NotImplementedError('Exception not raised!')
    except ValueError as error:
        assert isinstance(error, ValueError), 'Invalid Exception!'

