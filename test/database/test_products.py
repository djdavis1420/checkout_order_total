from src.database.products import get_all_products


def test_get_all_products__should_create_list_of_five_products():
    actual = get_all_products()
    assert len(actual) == 5


def test_get_all_products__should_have_only_one_soup_product_in_list():
    inventory = get_all_products()
    actual = [item for item in inventory if item.name == 'soup']
    assert len(actual) == 1
    assert actual[0].name == 'soup'
