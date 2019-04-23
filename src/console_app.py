from src.database.specials import get_special
from src.models.cart import Cart
from src.models.store import Store

store = Store()
cart = Cart()
store.stock_products()

by_unit = ['soup', 'soda', 'soap']
by_weight = ['beef', 'cheese']

shopping = True
while shopping is True:
    print('\nThe store has the following items available:\n')
    print([item.name for item in store.products])

    item_to_add = input('\nWhat would you like to add to your cart? Please type the name of the item (without quotes)\nas it appears in the list above, type REVIEW to review your cart, or type EXIT to exit.\n\n')

    if item_to_add == 'EXIT':
        break

    product_to_add = [product for product in store.products if product.name == item_to_add]
    amount_to_add = 0

    if item_to_add in by_unit:
        amount_to_add = input('\nHow many would you like to add to your cart? Please use standard integers (1, 2, 3, etc).\n\n')
        cart.add_product_by_unit(store, product_to_add[0], int(amount_to_add))
    elif item_to_add in by_weight:
        amount_to_add = input('\nHow much would you like to add to your cart? Please enter value in pounds, using standard floats (1.25 for 1.25 lb, .75 for .75 lb, 2.5 for 2.5 lbs, etc).\n\n')
        cart.add_product_by_weight(store, product_to_add[0], float(amount_to_add))
    elif (item_to_add not in by_unit) or (item_to_add not in by_weight):
        shopping = False

    reviewing = False
    if item_to_add == 'REVIEW':
        reviewing = True

    while reviewing is True:
        print('\nYou have the following items in your cart:\n')
        print([item.name for item in cart.products])

        action = input('\nWould you like to EDIT your cart or CHECKOUT?\n\n')

        if action == 'EDIT' and len(cart.products) != 0:
            item_to_remove = input('\nWhich item would you like to remove? Please type the name of the item (without quotes) as it appears in the list above.\n\n')
            number_to_remove = int(input('\nHow many would you like to remove? Please use standard integers (1, 2, 3, etc).\n\n'))
            cart.remove_product(item_to_remove, number_to_remove)
        elif action == 'EDIT' and len(cart.products) == 0:
            print('\nThere is nothing in your shopping cart.\n')
            reviewing = False
            shopping = True
        elif action == 'CHECKOUT' and len(cart.products) == 0:
            print('\nThere is nothing in your shopping cart.\n')
            reviewing = False
            shopping = True
        elif action == 'CHECKOUT' and len(cart.products) != 0:
            for item in cart.products:
                item.special_details = get_special(item.name)
                if item.special_details is not None:
                    item.has_special = True
            cart.parse_cart()
            total = cart.total_all_items()
            print('\nYour subtotal is: $' + str(total))
            reviewing = False
            shopping = False
