import pytest


from product.factories import CategoryFactory


@pytest.fixture
def category_create():
    return CategoryFactory(title="PyTest with Factory !!!")


@pytest.mark.django_db
def test_create_category(category_create):
    assert category_create.title == "PyTest with Factory !!!"
