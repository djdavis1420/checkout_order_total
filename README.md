# Checkout Order Total
 - This application emulates a grocery point-of-sale system.
 - Please refer to Kata Description for a full description of the requirements.

## Prerequisites

```
IntelliJ IDEA with Python Plugin (or PyCharm)
```

## Installing
- Clone the repository at "https://github.com/djdavis1420/checkout_order_total.git".
- In your terminal/shell, navigate to the project's root directory.
- Activate a virtual environment (ie, "source ./venv/Scripts/activate") .
    - pip install -Ur test_requirements.txt
- Pytest and Mock will be installed in the virtual environment.

## Defining Products
 - Five products are defined by default
    - Soup: $1.89 per 1 unit
    - Soda: $1.49 per 1 unit
    - Soap: $2.49 per 1 unit
    - Beef: $5.99 per 1 pound
    - Cheese: $2.38 per 1 pound 
 - To add additional products:
    - Open the products.csv file.
    - Add products in the same format as existing products
        - e.g., name, unit price, unit weight
    - A simpler way to add new products is a future feature

## Defining Specials
 - Three types of specials are defined by default
    - A "basic unit discount" special on soup
        - $0.20 off per unit, up to five times
    - A "buy x get y" special on soda
        - buy two, get one free (100% off), up to two times
    - A "buy x for y" special on soap
        - buy three for $5.00, up to two times
 - To add additional specials:
    - Open the specials.json file.
    - Using existing specials as examples, add specials in the same format as existing specials, in JSON format.
    - A simpler way to add new specials is a future feature

## Running the Console Application
 - Right-click on checkout_order_total/src/console_app.py
 - Select "Run 'console_app'"
 - Follow the prompts in the console

## Future Features
 - Error/Exception Handling
 - Adding New Products/Specials

## Built With

- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - Integrated Development Environment
- [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework for Python
- [mock](https://docs.python.org/dev/library/unittest.mock.html) - Testing Library for Python