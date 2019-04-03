from src.models.cart import Cart
from src.models.product import Product


def test_add_product__should_add_one_soup_to_cart():
    cart = Cart()
    soup = Product('soup', 1.89)
    cart.add_product(soup, 1)

    actual = cart.products

    assert len(actual) == 1


def test_add_product__should_add_three_soups_to_cart():
    cart = Cart()
    soup = Product('soup', 1.89)
    cart.add_product(soup, 3)

    actual = cart.products

    assert len(actual) == 3


def test_remove_product__should_remove_one_soup_from_cart_leaving_two():
    cart = Cart()
    soup = Product('soup', 1.89)
    cart.add_product(soup, 3)
    cart.remove_product(soup, 1)

    actual = cart.products

    assert len(actual) == 2


def test_remove_product__should_remove_two_soups_from_cart_leaving_one():
    cart = Cart()
    soup = Product('soup', 1.89)
    cart.add_product(soup, 3)
    cart.remove_product(soup, 2)

    actual = cart.products

    assert len(actual) == 1
