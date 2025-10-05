# ---------------------------------------------------------
# Name: Parth Bhavsar
# Student ID: u3311230
# Subject: IIT
# Assignment: [2nd - Python Fundamentals] Case Study 1 - Campus Café Checkout
# Date: 17/09/2025
# ---------------------------------------------------------

TAX_RATE = 0.10
STUDENT_DISCOUNT = 0.05

menu = {
    1: ("Coffee", 2.50, "Beverage"),
    2: ("Tea", 2.00, "Beverage"),
    3: ("Sandwich", 5.00, "Food"),
    4: ("Muffin", 3.00, "Snack"),
    5: ("Juice", 3.50, "Beverage"),
    6: ("Salad", 4.50, "Food")
}

cart = []

def show_menu():
    print("Menu:")
    for num, (item, price, category) in menu.items():
        print(f"{num}. {item} - ${price:.2f} ({category})")

def add_item():
    show_menu()
    try:
        choice = int(input("Enter item number: "))
        if choice in menu:
            cart.append(menu[choice])
            print(f"{menu[choice][0]} added to cart.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")

def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    subtotal = sum(item[1] for item in cart)
    categories = {item[2] for item in cart}
    print("Cart contents:")
    for item in cart:
        print(f"- {item[0]} ${item[1]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Categories in cart: {', '.join(categories)}")

def checkout():
    if not cart:
        print("Nothing to checkout.")
        return
    subtotal = sum(item[1] for item in cart)
    discount = 0
    if input("Are you a student? (y/n): ").lower() == "y":
        discount = subtotal * STUDENT_DISCOUNT
    subtotal_after_discount = subtotal - discount
    tax = subtotal_after_discount * TAX_RATE
    total = subtotal_after_discount + tax
    print("----- Receipt -----")
    for item in cart:
        print(f"{item[0]} - ${item[1]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"Student Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    cart.clear()

while True:
    print("\n1. Show menu\n2. Add item\n3. View cart\n4. Checkout\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        show_menu()
    elif choice == "2":
        add_item()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        checkout()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
