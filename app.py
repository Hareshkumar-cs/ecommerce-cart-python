from abc import ABC, abstractmethod

# Abstract Base Class → Abstraction
class Product(ABC):
    def __init__(self, name, price):
        self._name = name        # Encapsulation (_name = protected)
        self._price = price

    @abstractmethod
    def get_details(self):
        pass

    def get_price(self):
        return self._price


# Inheritance Example → Electronics
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    # Polymorphism (different implementation of get_details)
    def get_details(self):
        return f"{self._name} (Electronics) - ${self._price}, Warranty: {self.warranty} year(s)"


# Inheritance Example → Clothing
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    # Polymorphism
    def get_details(self):
        return f"{self._name} (Clothing) - ${self._price}, Size: {self.size}"


# Composition → CartItem contains a Product
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.get_price() * self.quantity

    def __str__(self):
        return f"{self.product.get_details()} x {self.quantity} = ${self.get_total_price()}"


# Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item.product._name != product_name]

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)

    def show_cart(self):
        if not self.items:
            print("🛒 Your cart is empty!")
        else:
            print("\n--- Your Cart ---")
            for item in self.items:
                print(item)
            print("Total = $", self.calculate_total())


# ===== DEMO USAGE =====
if __name__ == "__main__":
    # Create Products
    laptop = Electronics("Laptop", 1200, 4)
    juicer=Electronics("juicer", 5000, 8)
    tshirt = Clothing("T-Shirt", 25, "M")
    tshirt = Clothing("T-Shirt", 25, "l")
    paints=Clothing("paints", 50, "M")
    paints=Clothing("paints", 50, "l")
    phone = Electronics("Smartphone", 800, 1)

    # Create Cart
    cart = ShoppingCart()

    # Add Products
    cart.add_item(laptop, 5)
    cart.add_item(tshirt, 2)
    cart.add_item(juicer,2)
    cart.add_item(phone, 1)

    # Show Cart
    cart.show_cart()

    # Remove an Item
    cart.remove_item("T-Shirt")
    cart.show_cart()
