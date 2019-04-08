from src.models.product import Product


class TestProduct:

    def setup_method(self):
        self.soup = Product('soup', 1.89)
        self.beef = Product('beef', 5.99, .75)

    def test_calculate_product_cost__should_return_cost_based_on_standard_price_and_weight(self):
        actual = self.beef.calculate_product_cost()
        assert actual == 4.49
