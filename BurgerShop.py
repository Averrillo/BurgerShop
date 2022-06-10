class FoodItem:
    pass
    item_name = ""

    def __init__(self, item_name):
        self.item_name = item_name

    def display(self):
        print(f"{self.item_name} added to order")


class Burger(FoodItem):
    pass
    burger_menu = {'original': 5.99, 'cheeseburger': 6.99, 'double cheeseburger': 8.99}


class Drink(FoodItem):
    pass
    drink_menu = {'small': 1.50, 'medium': 2, 'large': 3}


class Side(FoodItem):
    pass
    side_menu = {'fries': 2, 'onion rings': 3, 'poutine': 3.50}


class Combo(FoodItem):
    pass


class Order:
    pass
    client_name = ""
    order_details = []
    total_cost = 0

    def __init__(self, client_name):
        self.client_name = client_name


def user_input_burger():

    burger = input("What kind of burger would you like original, cheeseburger or double cheeseburger: ")
    b = Burger(burger)
    b.display()
    # ask user for input and store it in burger object
    return b


def user_input_drink():
    d = Drink()
    # ask user for input and store it in drink object
    return d


def user_input_side():
    s = Side()
    # ask user for input and store it in side object
    return s


def user_input_combo():
    c = Combo()
    # ask user for input and store it in combo object
    # a combo must include one burger, one side, and one drink
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

    while(is_true):

        menu_num = input('1. Burgers\n2. Drinks\n3. Sides\n4. Combo\n5. Exit\n')
        if menu_num == '1':
            user_input_burger()

        elif menu_num == '2':
            user_input_drink()

        elif menu_num == '3':
            user_input_side()

        elif menu_num == '4':
            user_input_combo()

        elif menu_num == '5':
            break

        else:
            print("Please enter a valid number")














take_order()
