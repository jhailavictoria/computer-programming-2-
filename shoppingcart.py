class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print(f"{item.name} added to cart.")

    def remove_item(self, item_name):
        for item in self.cart:
            if item.name.lower() == item_name.lower():
                self.cart.remove(item)
                print(f"{item_name} removed from cart.")
                return
        print("Item not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\nItems in Cart:")
        for item in self.cart:
            print(f"{item.name} - Price: {item.price} x {item.quantity} = {item.total_price()}")

    def checkout(self):
        total = sum(item.total_price() for item in self.cart)
        print(f"\nTotal amount: {total}")
        print("Thank you for shopping!")
        self.cart.clear()


def main():
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Item name: ")
            price = float(input("Item price: "))
            quantity = int(input("Quantity: "))
            item = Item(name, price, quantity)
            cart.add_item(item)

        elif choice == "2":
            name = input("Enter item name to remove: ")
            cart.remove_item(name)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            cart.checkout()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

