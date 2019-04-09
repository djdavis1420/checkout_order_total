from src.database.specials import get_special


def test_get_special__should_return_dictionary_of_special_details():
    item_name = 'soup'
    special_details = {'specialType': 'basic unit discount', 'perUnitDiscount': 0.2, 'limit': 5}
    actual = get_special(item_name)
    assert actual == special_details