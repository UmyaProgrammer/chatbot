class Product:
    def __init__(self, name: str, amount: int, price: float):
        self.name = name
        self.amount= amount
        self.price = price


    def compare_price(self, pd2_price: float):
        return self.price > pd2_price


    def get_price(self):
        return self.price


    def get_amount(self):
        return self.amount


    def get_name(self):
        return self.name


    def return_product(self):
        self.amount += 1

    
    def checkout_product(self):
        self.amount -= 1


    def __str__(self):
        return f"Name: {self.name}\nAmount: {self.amount}\nPrice: ${self.price}"
        

class Shop:
    def __init__(self, products: list[Product]):
        self.products = products
        self.product_names = self.get_product_names()


    def print_products(self):
        for product in self.products:
            print(product)
            print()


    def get_product_names(self)->list[str]:
        list_of_names = []
        for product in self.products:
            list_of_names.append(product.get_name())

        return list_of_names


    def is_product(self, product_name: str)->bool:
        if product_name.lower() in [p.lower() for p in self.product_names]:
            return True
        return False

    
    def get_price_of_product(self, product_name: str)->float:
        for product in self.products:
            if product.get_name().lower() == product_name:
                return product.get_price()

    
    def return_product(self, product_name: str)->bool:
        for product in self.products:
            if product.get_name().lower() == product_name:
                initial_amount = product.get_amount()
                product.return_product()
                current_amount = product.get_amount()
                product_price = product.get_price()
            
        return current_amount > initial_amount, product_price


    def price_range_products(self, product_price: float):
        list_of_products_under_product_price = []

        for product in self.products:
            if product.get_price() <= product_price:
                list_of_products_under_product_price.append(product)
        
        for product in list_of_products_under_product_price:
            print(product)


    def exchange_product(self, product1_name: str, product2_name: str)->tuple[bool, float]:
        
        for product in self.products:
            if product.get_name().lower() == product1_name:
                p1 = product
            if product.get_name().lower() == product2_name:
                p2 = product

        if p1 and p2:
            can_exchange = False
            if p2.get_price() <= p1.get_price():
                return True, (p1.get_price() - p2.get_price())
            elif p2.get_price() > p1.get_price():
                return False, 1.1123
            else:
                return False, 0
            
        

    

