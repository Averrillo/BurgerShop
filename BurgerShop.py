import copy

CONDIMENTS = ['ketchup', 'mustard', 'mayo', 'onion', 'tomato', 'lettuce']
BURGER_MENU = {'original': 5.99, 'cheeseburger': 6.99, 'double cheeseburger': 8.99}
DRINK_MENU = {'coke', 'sprite', 'rootbeer'}
SIZE_MENU = {'small': 1.50, 'medium': 2, 'large': 3}
SIDE_MENU = {'fries': 2, 'onion rings': 3, 'poutine': 3.50}


class FoodItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    def get_price(self):
        return self.price

class Burger(FoodItem):

    def __init__(self, item_name, price):
        super().__init__(item_name, price)
        self.condiment_list = []

    def add_condiment(self, condiment):
        if condiment not in self.condiment_list:
            self.condiment_list.append(condiment)

    def getlist(self):
        return self.condiment_list

    def display(self):
        string = "Item: " + self.item_name + "\n" + "Price: " + str(self.price) + "$" + "\n" + "Condiments: " + ", ".join(self.condiment_list)
        return string


class Drink(FoodItem):
    def __init__(self, item_name, size, price):
        super(Drink, self).__init__(item_name, price)
        self.size = size

    def display(self):
        string = "Item: " + self.item_name + "\n" + "Price: " + str(self.price) + "$" + "\n" + "Size: " + self.size
        return string


class Side(FoodItem):
    def __init__(self, item_name, price):
        super(Side, self).__init__(item_name, price)

    def display(self):
        string = "Item: " + self.item_name + "\n" + "Price: " + str(self.price) + "$"
        return string


class Combo(FoodItem):

    DISCOUNT = .85

    def __init__(self, item_name, b, d, s, price):
        super().__init__(item_name, price)
        self.item_name = item_name
        self.Burger = b
        self.Drink = d
        self.Side = s
        self.price = (self.Burger.get_price() + self.Side.get_price() + self.Drink.get_price()) * self.DISCOUNT

    def display(self):
        string = "Item: " + self.item_name + "\n"
        string = string + str(self.Burger.item_name) + "\n" + str(self.Drink.item_name) + "\n" + str(self.Side.item_name) + "\n"
        string = string + "Combo price: " + str(self.price) + "\n"
        return string


class Order:
    client_name = ""
    order_list = []
    total_cost = 0

    def __init__(self, client_name):
        self.client_name = client_name

    def display(self):
        for i in self.order_list:
            print(i.display())

    def check_combo(self):
        burger_count = 0
        side_count = 0
        drink_count = 0

        for i in self.order_list:
            if isinstance(i, Burger):
                burger_count += 1
            elif isinstance(i, Side):
                side_count += 1
            elif isinstance(i, Drink):
                drink_count += 1
            else:
                print("There are not enough items to make a combo")



def user_input_burger():

    count = 0
    burger = input("What kind of burger would you like original, cheeseburger or double cheeseburger: ").lower()

    if burger in BURGER_MENU:
        price = BURGER_MENU[burger]
        b = Burger(burger, price)
    else:
        print("Sorry that is not on our menu")

    updated_condiment = copy.deepcopy(CONDIMENTS)
    print(f'Please choose up to three condiments: ')

    while count < 3:
        for i in updated_condiment:
            print(i)
        condiment = input("Enter condiment or done: ").lower()
        if condiment == 'done':
            break
        elif condiment not in updated_condiment:
            print("Sorry not in condiment list")
        else:
            b.condiment_list.append(condiment)
            updated_condiment.remove(condiment)
            count += 1

    print(b.condiment_list)

    return b


def user_input_drink():

    print("These are the drinks available")
    print(DRINK_MENU)
    print("these are the available sizes and their prices")
    print(SIZE_MENU)

    while True:
        temp = input("What drink would you want").lower()
        if temp in DRINK_MENU:
            drink_name = temp
            break
        else:
            print("Please enter a valid drink")

    while True:
        temp = input("What size drink do you want").lower()
        if temp in SIZE_MENU:
            drink_size = temp
            break
        else:
            print("Please enter a valid drink size")

    d = Drink(drink_name, drink_size, SIZE_MENU[drink_size])
    return d


def user_input_side():

    print("These are the sides available with their relative prices")
    print(SIDE_MENU)

    while True:
        side_name = input("What side would you want").lower()
        if side_name in SIDE_MENU:
            break
        else:
            print("Please enter a valid side")
    s = Side(side_name, SIDE_MENU[side_name])
    return s


def user_input_combo():
    print("Let's order your combo!")
    print("let's start with your burger.")
    b = user_input_burger()
    print("Now what would you like for a side")
    s = user_input_side()
    print("Lastly, what would you like for a drink")
    d = user_input_drink()
    c = Combo("Combo", b, d, s, 0)
    return c


def take_order():
    # ask user for name for the order
    # repeat taking order until client is done
    # display order details
    # display a thank you message
    is_true = True
    print("Welcome to Burger Shop")
    name = input("Can I get your name for the order: ")
    order = Order(name)
    print(f'Hello {order.client_name} choose a menu you would like to order from')

    while is_true:

        menu_num = input('1. Burgers\n2. Drinks\n3. Sides\n4. Combo\n5. Exit\n')
        if menu_num == '1':
            o = user_input_burger()
            order.order_list.append(o)

        elif menu_num == '2':
            o = user_input_drink()
            order.order_list.append(o)

        elif menu_num == '3':
            o = user_input_side()
            order.order_list.append(o)

        elif menu_num == '4':
            o = user_input_combo()
            order.order_list.append(o)

        elif menu_num == '5':
            order.check_combo()
            order.display()

            break

        else:
            print("Please enter a valid number")

take_order()