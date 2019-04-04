def basic_checkout(cart):
    total = 0
    for item in cart.products:
        item.calculate_cost()
        total += item.sale_price
    return round(total, 2)
