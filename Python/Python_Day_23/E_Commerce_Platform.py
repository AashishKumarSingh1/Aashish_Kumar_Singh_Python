class Product:

    def __init__(self,id:int,name,price:int,stock:int) -> None:
        self.id=id 
        self.name=name
        self.price=price
        self.stock=stock

    def __str__(self) -> str:
        return f"Product Name: {self.name} , Product Price:{self.price} , Product Stock:{self.stock}"

class Customer:

    def __init__(self,id,name,email) -> None:
        self.id=id 
        self.name=name
        self.email=email

    def __str__(self) -> str:
        return f"Customer Name:{self.name} , Customer email:{self.email} "

class Order:

    def __init__ (self,customer):
        self.customer=customer
        self.total_price=0.0
        self.products={}#dictionary 

    def add_product(self,product,quantity):
        if product.stock<quantity:
            raise ValueError(f"Product {product.name} is not in the stock!")
        
        if product.id in self.products:
            self.products[product.id]['quantity'] += quantity

        else:
            self.products[product.id] = {'product': product, 'quantity': quantity}
        
        product.stock -= quantity
        self.total_price += product.price * quantity

    def remove_product(self, product, quantity):

        if product.id not in self.products:
            raise ValueError(f"Product {product.name} is not in the order.")
        
        if self.products[product.id]['quantity'] < quantity:
            raise ValueError(f"Cannot remove {quantity} of {product.name}. Only {self.products[product.id]['quantity']} in order.")
        
        self.products[product.id]['quantity'] -= quantity
        product.stock += quantity
        self.total_price -= product.price * quantity
        
        if self.products[product.id]['quantity'] == 0:
            del self.products[product.id]

    def process_payment(self):
        print(f"Processing payment for {self.customer.name}")
        print(f"Total amount due: ${self.total_price:.2f}")
        self.products.clear()
        self.total_price = 0.0

    def __str__(self):
        order_details = f"Order for {self.customer.name}:\n"
        for item in self.products.values():
            order_details += f"{item['product'].name} (Quantity: {item['quantity']})\n"
        order_details += f"Total Price: ${self.total_price:.2f}"
        return order_details
    
if __name__=='__main__':
        
        # Create some products
        product1 = Product(1, "Laptop", 1000, 50)
        product2 = Product(2, "Smartphone", 500, 100)

        # Create a customer
        customer = Customer(1, "Alice", "alice@example.com")

        # Create an order for the customer
        order = Order(customer)

        # Add products to the order
        order.add_product(product1, 2)
        order.add_product(product2, 5)

        # Print order details
        print(order)

        # Remove a product from the order
        order.remove_product(product2, 2)

        # Print order details after removal
        print(order)

        # Process payment
        order.process_payment()

        # Print order details after processing payment
        print(order)
