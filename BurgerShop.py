import copy

class FoodItem:
    pass
    item_name = ""
    number = 0

    def __init__(self, item_name, number):
        self.item_name = item_name
        self.number = number

    def display(self):
        print(f"{self.item_name} added to order")



class Burger(FoodItem):

    condiment_list = []
    condiment_menu = ['ketchup', 'mustard', 'mayo', 'onion', 'tomato', 'lettuce']
    burger_menu = {'original': 5.99, 'cheeseburger': 6.99, 'double cheeseburger': 8.99}

    def emptylist(self):
        self.condiment_list = []

    def getlist(self):
        return self.condiment_list


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
    order_list = []
    total_cost = 0

    def __init__(self, client_name):
        self.client_name = client_name

    def display_amount(self):
        for i in self.order_list:
            print(f'You ordered {i.number} {i.item_name}')


def user_input_burger():

    count = 0
    burger = input("What kind of burger would you like original, cheeseburger or double cheeseburger: ").lower()
    number = input("How many would you like").lower()
    b = Burger(burger, number)
    b.emptylist()

    updated_condiment = copy.deepcopy(b.condiment_menu)
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

    drink = input()
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
            order.display_amount()
            break

        else:
            print("Please enter a valid number")

    for i in order.order_list:
        print(i.getlist())














take_order()

