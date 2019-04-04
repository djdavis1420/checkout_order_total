def basic_checkout(cart):
    total = 0
    for item in reversed(cart.products):
        item.calculate_product_cost()
        total += item.sale_price
        cart.scanned.append(item)
        cart.products.remove(item)
    return round(total, 2)
