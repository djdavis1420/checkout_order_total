from src.models.product import Product


def test_set_discount__should_reduce_soup_price_by_twenty_cents():
    soup = Product('soup', 1.89)
    soup.set_discount(.20)

    actual = soup.discount_price

    assert actual == 1.69
