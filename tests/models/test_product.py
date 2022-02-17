import pytest


from product.factories import ProductFactory


@pytest.fixture
def product_create():
    return ProductFactory(title="PyTest with Factory !!!")


@pytest.mark.django_db
def test_create_product(product_create):
    assert product_create.title == "PyTest with Factory !!!"
