from shop import Product, Shop
from random import choice
from store_products import products


class Chatbot:
    def __init__(self, fname: str, lname: str, age: int):
        self.user_fname = fname
        self.user_lname = lname
        self.user_age = age
        self.number_of_texts = 0
        self.options = ["exchange", "exit", "return", "options", "products"]
        self.shop = self._create_shop()


    def greet(self):
        print(f"Welcome {self.user_fname} {self.user_lname}!\n\n")


    def farewell(self):
        farewell_messages = [
            f"Goodbye, {self.user_fname} {self.user_lname}! Hope to see you again soon.",
            f"Take care, {self.user_fname} {self.user_lname}. Thanks for stopping by!",
            f"Farewell, {self.user_fname} {self.user_lname}! Wishing you all the best ahead.",
            f"It was great having you, {self.user_fname} {self.user_lname}. Come back anytime!",
            f"Goodbye for now, {self.user_fname} {self.user_lname}. Stay safe and take it easy!",
            f"See you next time, {self.user_fname} {self.user_lname}! Have a great day!",
            f"All the best, {self.user_fname} {self.user_lname}. Until we meet again!",
            f"Thanks for visiting, {self.user_fname} {self.user_lname}. Hope you enjoyed your time here!",
            f"Wishing you well, {self.user_fname} {self.user_lname}! Don’t be a stranger.",
            f"Goodbye, {self.user_fname} {self.user_lname}! May your next visit be even better!"
        ]

        print(choice(farewell_messages))


    def options_list(self):
        print(f"Here are the options:\n\tReturn an item - (return)\n\tExchange an item - (exchange)\n\t(products) for products\n\t(options) for a list of options\n\t(exit) to exit\n")


    def validate_product(self, i: int)->str:
        if i == 1:
            user_product = input("Please enter the name of the product you would like to return!\n: ")
        elif i == 2:
            user_product = input("Please enter the name of the product you would like to exchange it to!\n: ")
        elif i == 3:
            user_product = input("Product: ")
        else:
            user_product = input("Let's try a different product: ")
        
        # To create a space between two chats.
        print()

        if user_product == "exit":
            return user_product

        while not self.shop.is_product(user_product):
            user_product = input("Please enter a valid product name!\n: ")
        
        
        return user_product


    def _create_shop(self)->Shop:
        # Creating a shop object to continue with the function
        list_of_products = []

        for product in products:
            new_product = Product(product["name"], product["amount"], product["price"])
            list_of_products.append(new_product)

        shop = Shop(list_of_products)
        return shop


    def exchange_too_expensive(self, p1: str)->bool:
        price_difference_messages = [
            "It looks like the item you're exchanging for costs a bit more than your original purchase.",
            "The new product has a higher price than the one you're returning.",
            "This exchange involves an additional cost, as the replacement item is more expensive.",
            "The item you selected costs more than the one being returned — a price difference applies.",
            "Please note: the new product's price is higher than your original item.",
            "There's a small price difference — the new item is more expensive than the returned one.",
            "You've chosen an upgraded product that costs more than your previous purchase.",
            "This exchange will require an additional payment since the new item is pricier.",
            "The replacement you selected is at a higher price point than your returned item.",
            "A payment adjustment is needed — the new product costs more than your return."
        ]


        print(f"{self.user_fname}! The product you chose to get in exchange is far more expensive, please try exchanging again, but next time choose less than {self.shop.get_price_of_product(p1)}")
        user_choice = input("Would you like to exchange your returned product into different one?(y/n) ").lower()
        
        if user_choice == "y":
            new_exchange_product = self.validate_product(3)
            success, change = self.shop.exchange_product(p1, new_exchange_product)
            
            while change == 1.1123:
                print(choice(price_difference_messages))
                new_exchange_product = self.validate_product(4)
                success, change = self.shop.exchange_product(p1, new_exchange_product)

            return True, change
        return False, 0
    
    
    def return_convo(self, item: str):
        print("Give me a second, just making sure that is the right thing.")
        print("Yup it is, now we can get to returning.")

        success, price = self.shop.return_product(item)

        messages = [
            f"Congratulations {self.user_fname}! You've successfully returned the item {item}. ${price} has been successfully deposited to your account.",
            f"The item {item} has been successfully returned — thank you for completing the process. ${price} has been successfully deposited to your account.",
            f"Great job! Your return of {item} is complete — one less thing on your to-do list! ${price} has been successfully deposited to your account."
        ]
        
        if success:
            print(choice(messages))
        else:
            print(f"Hmm, I think an error occured {self.user_fname}! Let us restart your process. Click (y) on the next question!")
    

    def exchange_convo(self, item: str):
        exchange_product = self.validate_product(2)

        messages = [
            f"Congratulations {self.user_fname}! You've successfully returned the item {item} in exchange for {exchange_product}.",
            f"The item {item} has been successfully returned in exchange for {exchange_product}— thank you for completing the process.",
            f"Great job! Your return of {item} in exchange for {exchange_product} is completed — one less thing on your to-do list!"
        ]

        success, change = self.shop.exchange_product(item, exchange_product)
        if success:
            print(f"{choice(messages)}\nYour change of ${change} has been sent to your account!")
        
        elif change == 1.1123:
            success, change = self.exchange_too_expensive(item)
            if success:
                print(f"{choice(messages)}\nYour change of ${change} has been sent to your account!")
                
        else:
            print(f"Hmm, I think an error occured {self.user_fname}! Let us restart your process. Click (y) on the next question!")


    def start_conversation(self)->bool:
        print(f"How may I help you today?")
        
        user_choice = input(": ")
        while user_choice.lower() not in self.options:
            user_choice = input("Please enter a valid command:\n\tReturn an item - (return)\n\tExchange an item - (exchange)\n\t(products) for products\n\t(options) for a list of options\n\t(exit) to exit\n: ")


        if user_choice.lower() == "return":
            user_product = self.validate_product(1)
            self.return_convo(user_product)
            print()
        elif user_choice.lower() == "exchange":
            user_product = self.validate_product(1)
            self.exchange_convo(user_product)
            print()
        elif user_choice.lower() == "products":
            self.shop.print_products()
            print()
        elif user_choice.lower() == "options":
            self.options_list()
            print()
        else:
            return False
        
        return True

    
    def continue_conversation(self)->bool:
        continue_messages = [
            f"Is there anything else you'd like to do, {self.user_fname}?",
            f"What would you like to do next, {self.user_fname}?",
            f"Anything else on your mind, {self.user_fname}?",
            f"How can I help you further, {self.user_fname}?",
            f"Would you like to try something else, {self.user_fname}?",
            f"What's next on your list, {self.user_fname}?",
            f"Need help with something else, {self.user_fname}?",
            f"Shall we do something else, {self.user_fname}?",
            f"What should we do next, {self.user_fname}?",
            f"Is there anything more I can assist with, {self.user_fname}?"
        ]


        print(choice(continue_messages))
        
        user_choice = input(": ")
        while user_choice.lower() not in self.options:
            user_choice = input("Please enter a valid command:\n\tReturn an item - (return)\n\tExchange an item - (exchange)\n\t(products) for products\n\t(options) for a list of options\n\t(exit) to exit\n: ")


        if user_choice.lower() == "return":
            user_product = self.validate_product(1)
            self.return_convo(user_product)
            print()
        elif user_choice.lower() == "exchange":
            user_product = self.validate_product(1)
            self.exchange_convo(user_product)
            print()
        elif user_choice.lower() == "products":
            self.shop.print_products()
            print()
        elif user_choice.lower() == "options":
            self.options_list()
            print()
        else:
            return False
        
        return True