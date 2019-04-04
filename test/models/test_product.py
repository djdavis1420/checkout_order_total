from src.models.product import Product


class Test:

    def setup_method(self):
        self.soup = Product('soup', 1.89)
        self.beef = Product('beef', 5.99, .75)

    def test_set_discount__should_reduce_soup_price_by_twenty_cents(self):
        self.soup.set_discount(.20)
        actual = self.soup.discount_price
        assert actual == 1.69

    def test_calculate_cost__should_return_cost_based_on_standard_price_and_weight(self):
        actual = self.beef.calculate_cost()
        assert actual == 4.49

    def test_calculate_cost__should_return_cost_based_on_discount_price_and_weight(self):
        self.beef.set_discount(.50)
        actual = self.beef.calculate_cost()
        assert actual == 4.12
