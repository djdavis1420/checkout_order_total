from src.database.specials import get_special


def basic_unit_discount(cart, item_name):
    special_details = get_special(item_name)
    products = [product for product in cart.special_items if product.name == item_name]
    limit = special_details['limit']
    total = 0
    for item in products:
        limit -= 1
        if limit >= 0:
            item.discount_price = item.unit_price - special_details['perUnitDiscount']
            item.sale_price = item.discount_price
        elif limit < 0:
            item.sale_price = item.unit_price
        total += item.sale_price
    return total
