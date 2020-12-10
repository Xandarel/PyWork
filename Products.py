from abc import ABC


class Product(ABC):
    def __init__(self, sku, price, name, quantity, brand):
        self.sku = sku
        self.price = price
        self.name = name
        self.quantity = quantity
        self.brand = brand


    def show_product(self):
        return f'\tid - {self.sku}\n\tprice - {self.price}\n\tname - {self.name}\n\tquantity - {self.quantity}\n\tbrand - {self.brand}\n\t'


class TshirtProduct(Product):
    def __init__(self, sku, price, name, quantity, brand, size, color):
        super().__init__(sku, price, name, quantity, brand)
        self.size = size
        self.color = color

    def dict_product(self):
        return {'id': self.sku, 'price': self.price, 'name': self.name, 'quantity': self.quantity,
                'brand': self.brand, 'size': self.size, 'color': self.color}

    def show_product(self):
        return super().show_product() + f'size - {self.size}\n\tcolor - {self.color}\n\t'


class SneakersProduct(Product):
    def __init__(self, sku, price, name, quantity, brand, size, color):
        super().__init__(sku, price, name, quantity, brand)
        self.size = size
        self.color = color

    def dict_product(self):
        return {'id': self.sku, 'price': self.price, 'name': self.name, 'quantity': self.quantity,
                'brand': self.brand, 'size': self.size, 'color': self.color}

    def show_product(self):
        return super().show_product() + f'size - {self.size}\n\tcolor - {self.color}'

