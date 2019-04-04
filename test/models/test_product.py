from src.models.product import Product


def test_set_discount__should_reduce_soup_price_by_twenty_cents():
    soup = Product('soup', 1.89)
    soup.set_discount(.20)

    actual = soup.discount_price

    assert actual == 1.69


def test_calculate_cost__should_return_cost_based_on_standard_price_and_weight():
    beef = Product('beef', 5.99)
    weight = .75

    actual = beef.calculate_cost(weight)

    assert actual == 4.49


def test_calculate_cost__should_return_cost_based_on_discount_price_and_weight():
    beef = Product('beef', 5.99)
    beef.set_discount(.50)
    weight = .75

    actual = beef.calculate_cost(weight)

    assert actual == 4.12
