class Item:

    def __init__(self,id,name,price,quantity) -> None:
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self) -> str:
        return f"Name:{self.name} , Id:{self.id} , Price: {self.price} , Quantity: {self.quantity}"
    
class Inventory:

    def __init__(self) -> None:
        self.items={}
    
    def add_item(self,item):
        if item.id in self.items:
            raise ValueError(f"Item with item_id({item.id}) exist!")
        self.items[item.id]=item

    def remove_item(self,id):
        if id in self.items:
            del self.items[id]
        else:
            raise ValueError(f"Item with id {item.id} does not exist!")
        
    def update_item(self,item,name=None,id=None , quantity=None,price=None):
        if name is not None:
            self.name=name
        if id is not None:
            self.id=id 
        if quantity is not None:
            self.quantity=quantity
        if price is not None:
            self.price=price
        
    def search_item(self,id):
        return self.items.get(id, None)
    
    def total_value(self):
        return sum((item.price*item.quantity for item in self.items.values() ))
    
    def generate_report(self):
        result='Inventory List' + '\n'
        for item in self.items:
            result=str(item) + "\n"
        return result

# Create some items
item1 = Item(1, "Laptop", 1000, 10)
item2 = Item(2, "Smartphone", 500, 20)
item3 = Item(3, "Tablet", 300, 15)

# Create an inventory
inventory = Inventory()

# Add items to the inventory
inventory.add_item(item1)
inventory.add_item(item2)
inventory.add_item(item3)

# Generate a report on inventory levels
print(inventory.generate_report())

# Calculate the total value of the inventory
print(f"Total Inventory Value: ${inventory.total_value()}")

# Search for an item
print(inventory.search_item(2))

# Update an item's information
inventory.update_item(2, price=550, quantity=18)
print(inventory.search_item(2))

# Remove an item from the inventory
inventory.remove_item(3)
print(inventory.generate_report())
print(f"Total Inventory Value: ${inventory.total_value()}")



# hello={}#dictionary 
# hello1=set()#set
# print(type(hello1))

# item1=Item(1,'Laptop',10,1)
# print(item1)
        