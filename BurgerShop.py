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
    pass
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

    def __init__(self, burger, side, drink):
        self.burger = burger
        self.side = side
        self.drink = drink
        
    



class Order:
    pass
    client_name = ""
    order_list = []

    def __init__(self, client_name):
        self.client_name = client_name

    def display_amount(self):
        for i in self.order_list:
            
            if isinstance(i, Burger):
                print(f'You ordered {i.number} {i.item_name} with condiments {i.condiment_list}')
            else:
                print(f'You ordered {i.number} {i.item_name}')
            
    def display_total_cost(self):
        total_cost = 0
        for j in self.order_list:
            total_cost += j.cost
        print(f'Your total cost is {total_cost}')
            

def user_input_burger():

    count = 0
    burger = input("What kind of burger would you like original, cheeseburger or double cheeseburger: ").lower()
    number = input("How many would you like ").lower()
    b = Burger(burger, number)
    b.emptylist()
    
    b.cost = int(number) * b.burger_menu[burger]
    print(str(b.cost))
    
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

    return b


def user_input_drink():

    drink = input("Would you like a small, medium or large drink? ").lower()
    number = input("How many would you like? ").lower()
    
    d = Drink(drink, number)
    d.cost = int(number) * d.drink_menu[drink]
    print(str(d.cost))
    # ask user for input and store it in drink object
    return d


def user_input_side():
    
    side = input("Would you like a fries, onion rings, or poutine? ").lower()
    number = input("How many would you like? ").lower()
    
    s = Side(side, number)
    s.cost = int(number) * s.side_menu[side]
    print(str(s.cost))
    
    # ask user for input and store it in side object
    return s


def user_input_combo():
    
    count = 0
    burger_type = input("What kind of burger would you like original, cheeseburger or double cheeseburger: ").lower()
    burger = Burger(burger_type, 1)
    burger.cost = burger.burger_menu[burger_type]
    
    updated_condiment = copy.deepcopy(burger.condiment_menu)
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
            burger.condiment_list.append(condiment)
            updated_condiment.remove(condiment)
            count += 1
    
    
    side_type = input("Would you like a fries, onion rings, or poutine? ").lower()
    side = Side(side_type, 1)
    side.cost = side.side_menu[side_type]
    
    drink_size = input("Would you like a small, medium or large drink? ").lower()
    drink = Drink(drink_size, 1)
    drink.cost = drink.drink_menu[drink_size]
    
    combo_list = [burger, side, drink]
    
    c = Combo(burger, side, drink)
    c.item_name = f"Combo with {burger.item_name}, {side.item_name}, and {drink.item_name}"
    c.number = 1
    
    c.init_combo_cost = 0
    
    for item in combo_list:
        
        c.init_combo_cost += int(item.cost)
        
    c.cost = c.init_combo_cost * 0.85
    
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
    print(f'Hello, {order.client_name}! Choose a menu you would like to order from. Note: combo orders are 15% off! ')

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
            order.display_total_cost()
            break

        else:
            print("Please enter a valid number")


take_order()