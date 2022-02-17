import pytest

from order.factories import OrderFactory, UserFactory


@pytest.fixture
def user_create():
    return UserFactory(username="PyTest with Factory !!!")


@pytest.fixture
def order_create(user_create):
    return OrderFactory(user=user_create)


@pytest.mark.django_db
def test_create_order(order_create):
    print(order_create.user.username)
    assert order_create.user.username == "PyTest with Factory !!!"
