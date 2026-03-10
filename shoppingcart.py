cart = {}

def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if item in cart:
        cart[item]["quantity"] += quantity
    else:
        cart[item] = {"price": price, "quantity": quantity}

    print(item, "added to cart.\n")


def remove_item():
    item = input("Enter item to remove: ")

    if item in cart:
        del cart[item]
        print(item, "removed.\n")
    else:
        print("Item not found.\n")


def view_cart():
    total = 0
    print("\n--- Shopping Cart ---")

    for item, details in cart.items():
        price = details["price"]
        quantity = details["quantity"]
        subtotal = price * quantity
        total += subtotal

        print(f"{item} | Price: {price} | Qty: {quantity} | Subtotal: {subtotal}")

    print("Total:", total)
    print()


def checkout():
    view_cart()
    print("Thank you for shopping!")
    exit()


while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")

    choice = input("Choose option: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        remove_item()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        checkout()

    else:
        print("Invalid option\n")