from src.database.specials import get_special


def basic_unit_discount(cart, item_name):
    special_details = get_special(item_name)
    products = [product for product in cart.special_items if product.name == item_name]
    limit = special_details['limit']
    total_price = 0
    for product in products:
        limit -= 1
        if limit >= 0:
            product.discount_price = product.unit_price - special_details['perUnitDiscount']
            product.sale_price = product.discount_price
        elif limit < 0:
            product.sale_price = product.unit_price
        total_price += product.sale_price
    return round(total_price, 2)


def buy_x_get_y(cart, item_name):
    special_details = get_special(item_name)
    products = [product for product in cart.special_items if product.name == item_name]
    limit = special_details['limit']
    count = len(products)
    standard_price = products[0].unit_price
    special_price = (standard_price - (standard_price * (special_details['z'] / 100)))
    products_at_standard_price = 0
    products_at_special_price = 0
    total_price = 0

    if (limit == 0) or (limit is None):
        limit = 99999

    while count > 0 and limit > 0:
        buy_count = 0
        get_count = 0
        while buy_count < special_details['x'] and limit > 0 and count > 0:
            products_at_standard_price += 1
            buy_count += 1
            count -= 1
        while get_count < special_details['y'] and limit > 0 and count > 0:
            products_at_special_price += 1
            get_count += 1
            count -= 1
        limit -= 1
    products_at_standard_price += count

    total_at_standard_price = products_at_standard_price * standard_price
    total_at_special_price = products_at_special_price * special_price
    total_price = total_at_standard_price + total_at_special_price

    return round(total_price, 2)


def buy_x_for_y(cart, item_name):
    special_details = get_special(item_name)
    products = [product for product in cart.special_items if product.name == item_name]
    standard_price = products[0].unit_price
    special_price = special_details['y']

    products_at_special_price = len(products) // special_details['x']
    products_at_standard_price = len(products) % special_details['x']

    if products_at_special_price > special_details['limit']:
        difference = products_at_special_price - special_details['limit']
        products_at_special_price = special_details['limit']
        difference = difference * 3
        products_at_standard_price += difference

    total_at_standard_price = products_at_standard_price * standard_price
    total_at_special_price = products_at_special_price * special_price
    total_price = total_at_special_price + total_at_standard_price

    return round(total_price, 2)

