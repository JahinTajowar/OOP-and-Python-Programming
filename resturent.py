from abc import ABC

class User(ABC):
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Employees(User):
    def __init__(self, name, email, phone, address, salary, job):
        super().__init__(name, email, phone, address)
        self.salary = salary
        self.job = job

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def add_to_cart(self, restaurant, item, quantity):
        itm = restaurant.menu.find_item(item)
        if itm:
            if quantity > itm.quantity:
                print("Item quantity exceeded!!")
            else:
                itm.quantity -= quantity
                self.cart.add_to_cart(Item(itm.name, itm.price, quantity))
                print("Item added")
        else:
            print(f"{item} is not available in {restaurant.name}")

    def show_cart(self):
        print("<---------------View Cart-------------------->")
        print("Name\tPrice\tQuantity")
        for item in self.cart.items:
            print(f"{item.name}\t{item.price} $\t{item.quantity}")
        print("Total price:", self.cart.total_price)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def pay_bill(self):
        self.cart.clear()
        print("Bill paid and cart cleared.")

class Order:
    def __init__(self):
        self.items = []

    def add_to_cart(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                break
        else:
            print(f"{item_name} is not available in cart")

    @property
    def total_price(self):
        return sum(item.price * item.quantity for item in self.items)

    def clear(self):
        self.items = []

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employees(self, restaurant, employee):
        restaurant.add_employees(employee)
        print(f"{employee.name} added!!")

    def display_employees(self, restaurant):
        restaurant.display_employees()

    def show_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_item(self, restaurant, item):
        restaurant.menu.add_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employees(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print("<---------------Employees List---------------->")
        for employee in self.employees:
            print(f"{employee.name}\t{employee.email}\t{employee.phone}\t{employee.address}\t{employee.salary}\t{employee.job}")

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item.name} removed!!")
        else:
            print(f"{item_name} not found!!")

    def show_menu(self):
        print("<---------------Menu---------------->")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price} $\t{item.quantity}")

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

restaurant = Restaurant("Mamar Restaurant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    customer = Customer(name, email, phone, address)
    while True:
        print("<--------Customer Menu--------->")
        print("1. Add to cart")
        print("2. View cart")
        print("3. Show menu")
        print("4. Pay bill")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            customer.add_to_cart(restaurant, item_name, quantity)
        elif choice == 2:
            customer.show_cart()
        elif choice == 3:
            customer.view_menu(restaurant)
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    admin = Admin(name, email, phone, address)
    while True:
        print("<--------Admin Menu---------->")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. Display employees")
        print("4. Show items")
        print("5. Delete items")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            item = Item(item_name, item_price, quantity)
            admin.add_item(restaurant, item)
        elif choice == 2:
            name = input("Enter employee name: ")
            email = input("Enter employee email address: ")
            phone = input("Enter employee phone number: ")
            address = input("Enter employee address: ")
            salary = input("Enter employee salary: ")
            job = input("Enter employee position: ")
            employee = Employees(name, email, phone, address, salary, job)
            admin.add_employees(restaurant, employee)
        elif choice == 3:
            admin.display_employees(restaurant)
        elif choice == 4:
            admin.show_menu(restaurant)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(restaurant, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

while True:
    print("Welcome to ABC Restaurant!")
    print("1. Login as Admin")
    print("2. Login as Customer")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
