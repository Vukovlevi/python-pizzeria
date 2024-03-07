class Pizza():
    def __init__(self, name, components, recipe, toppings, price) -> None:
        self.name = name
        self.components = components
        self.recipe = recipe
        self.toppings = toppings.split(",")
        self.price = price

class User():
    def __init__(self, name, username, password, address, phone_number, email_address):
        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.phone_number = phone_number,
        self.email_address = email_address

class Order():
    def __init__(self, pizza, user, count):
        self.pizza = pizza
        self.user = user
        self.price = pizza.price * count