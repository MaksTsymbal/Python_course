# Write a class Product that has three attributes:
#
#     type
#     name
#     price
#
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
#
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
# additional classes to operate on a certain type of product, etc.
#
# Also, the ProductStore class must have the following methods:
#
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your
# store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
# identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        if amount <= 0:
            raise ValueError("Amount should be a positive integer.")
        self.products.append({'product': product, 'amount': amount, 'price': product.price * 1.3})

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent <= 0:
            raise ValueError("Discount percentage should be a positive number.")
        for p in self.products:
            if identifier_type == 'name' and p['product'].name == identifier:
                p['price'] *= (1 - percent / 100)
            elif identifier_type == 'type' and p['product'].type == identifier:
                p['price'] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for p in self.products:
            if p['product'].name == product_name:
                if p['amount'] < amount:
                    raise ValueError("Not enough products in stock.")
                p['amount'] -= amount
                income = p['price'] * amount
                return income
        raise ValueError("Product not found.")

    def get_income(self):
        total_income = 0
        for p in self.products:
            total_income += (p['price'] * p['amount'])
        return total_income

    def get_all_products(self):
        return [(p['product'].type, p['product'].name, p['amount'], p['price']) for p in self.products]

    def get_product_info(self, product_name):
        for p in self.products:
            if p['product'].name == product_name:
                return (p['product'].name, p['amount'])
        raise ValueError("Product not found.")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
print(s.get_product_info('Ramen') == ('Ramen', 290))
print(s.get_product_info('Ramen'))
print(s.get_all_products())
