class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"MenuItem(ID: {self.item_id}, Name: {self.name}, Price: ${self.price:.2f})"


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, menu_item, quantity):
        if menu_item.item_id in self.items:
            self.items[menu_item.item_id]['quantity'] += quantity
        else:
            self.items[menu_item.item_id] = {'item': menu_item, 'quantity': quantity}

    def remove_item(self, menu_item, quantity):
        if menu_item.item_id in self.items:
            self.items[menu_item.item_id]['quantity'] -= quantity
            if self.items[menu_item.item_id]['quantity'] <= 0:
                del self.items[menu_item.item_id]

    def calculate_total(self):
        total = sum(item['item'].price * item['quantity'] for item in self.items.values())
        return total

    def __str__(self):
        order_details = [f"{item['item'].name} x {item['quantity']}: ${item['item'].price * item['quantity']:.2f}"
                         for item in self.items.values()]
        return "\n".join(order_details)


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.orders = []
        self.inventory = {}

    def add_menu_item(self, item_id, name, price, quantity):
        menu_item = MenuItem(item_id, name, price)
        self.menu[item_id] = menu_item
        self.inventory[item_id] = quantity

    def update_menu_item(self, item_id, name=None, price=None, quantity=None):
        if item_id in self.menu:
            if name is not None:
                self.menu[item_id].name = name
            if price is not None:
                self.menu[item_id].price = price
            if quantity is not None:
                self.inventory[item_id] = quantity

    def place_order(self, order):
        for item_id, item_info in order.items.items():
            if item_id in self.inventory and self.inventory[item_id] >= item_info['quantity']:
                self.inventory[item_id] -= item_info['quantity']
            else:
                raise ValueError(f"Insufficient quantity for item ID {item_id}")
        self.orders.append(order)

    def generate_bill(self, order):
        total = order.calculate_total()
        return total

    def __str__(self):
        menu_details = [str(item) for item in self.menu.values()]
        return "\n".join(menu_details)


# Test cases
if __name__ == "__main__":
    restaurant = Restaurant()

    # Add menu items
    restaurant.add_menu_item(1, "Burger", 5.99, 10)
    restaurant.add_menu_item(2, "Pizza", 8.99, 5)
    restaurant.add_menu_item(3, "Salad", 4.99, 15)

    print("Menu Items:")
    print(restaurant)

    # Create an order
    order1 = Order()
    order1.add_item(restaurant.menu[1], 2)
    order1.add_item(restaurant.menu[2], 1)

    # Place order
    restaurant.place_order(order1)

    print("\nOrder 1 Details:")
    print(order1)
    print(f"Total Bill: ${restaurant.generate_bill(order1):.2f}")

    # Update menu items
    restaurant.update_menu_item(1, price=6.49)
    restaurant.update_menu_item(3, quantity=20)

    print("\nUpdated Menu Items:")
    print(restaurant)

    # Create another order
    order2 = Order()
    order2.add_item(restaurant.menu[1], 1)
    order2.add_item(restaurant.menu[3], 2)

    # Place order
    restaurant.place_order(order2)

    print("\nOrder 2 Details:")
    print(order2)
    print(f"Total Bill: ${restaurant.generate_bill(order2):.2f}")

    # Check inventory
    print("\nCurrent Inventory:")
    print(restaurant.inventory)
