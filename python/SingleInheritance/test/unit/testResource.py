from classes import Resource

import pytest


@pytest.fixture
def resource_values():
    return {'name': 'Test', 'manufacture': 'Test', 'total': 100, 'allocated': 50}


@pytest.fixture
def resource(resource_values):
    return Resource(**resource_values)


def test_create_resource(resource_values, resource):
    for key, value in resource_values.items():
        assert value == getattr(resource, key)


def test_float_total():
    with pytest.raises(TypeError):
        obj = Resource('Test', 'Intel', 10.1, 10)


def test_float_allocated():
    with pytest.raises(TypeError):
        obj = Resource('Test', 'Intel', 10, 9.3)


def test_excessive_allocation():
    with pytest.raises(ValueError):
        obj = Resource('Test', 'Intel', 10, 11)


def test_free_more_than_allocated():
    free = 11
    with pytest.raises(ValueError):
        obj = Resource('Test', 'Intel', 10, 10)
        obj.freed_up(free)

@pytest.mark.parametrize('dead', [-1,0 , 1000])
def test_invalid_died(dead):
    with pytest.raises(ValueError):
        obj :Resource= Resource('Test' , 'Intel', 10 , 1)
        obj.died(dead)


@pytest.mark.parametrize('total, allocated', [(-10, 10), (10, -10)])
def negative_total_and_allocated(total, allocated):
    with pytest.raises(ValueError):
        Resource('Tesat', 'Intel', total, allocated)
