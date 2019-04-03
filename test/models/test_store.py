from src.models.store import Store
from src.models.product import Product


def test_is_product_available__should_be_false():
    store = Store()
    soup = Product('soup', 1.89)

    actual = store.is_product_available(soup)

    assert actual is False


def test_is_product_available__should_be_true():
    store = Store()
    soup = Product('soup', 1.89)
    store.stock_product(soup)

    actual = store.is_product_available(soup)

    assert actual is True


def test_stock_product__should_be_true():
    store = Store()
    soup = Product('soup', 1.89)
    store.stock_product(soup)

    assert soup in store.products


def test_stock_product__should_be_false():
    store = Store()
    soup = Product('soup', 1.89)

    assert soup not in store.products


def test_discontinue_product__soup_should_no_longer_be_available():
    store = Store()
    soup = Product('soup', 1.89)
    beef = Product('beef', 5.99)
    store.stock_product(soup)
    store.stock_product(beef)
    store.discontinue_product(soup)

    actual = store.products

    assert soup not in actual

