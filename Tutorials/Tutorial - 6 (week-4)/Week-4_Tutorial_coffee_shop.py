# ...existing code...
print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
print(f"Hello, {customer_name}! Let's order some coffee.")

# ask if the customer is a university student and validate answer
is_student = None
while is_student is None:
    resp = input("Are you a university student? (yes/no): ").strip().lower()
    if resp in ("yes", "y"):
        is_student = True
    elif resp in ("no", "n"):
        is_student = False
    else:
        print("Please answer 'yes' or 'no'.")

price_coffee = 3.50
price_latte = 4.00
price_hot_chocolate = 5.00
price_espresso = 2.50

print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Hot Chocolate: $" + str(price_hot_chocolate))
print("Espresso: $" + str(price_espresso))
print("Please note: If you order more than one cup, you will receive a $1.00 discount on your total for that drink.")

# start a loop so the customer can order multiple drinks
total_cost = 0.0
more_drinks = "yes"

while more_drinks == "yes":
    choice = input("What would you like to order? (coffee/latte/hot chocolate/espresso): ").strip().lower()

    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "hot chocolate":
        cost = price_hot_chocolate
    elif choice == "espresso":
        cost = price_espresso
    else:
        print("Sorry, we do not have that.")
        cost = 0.0

    if cost > 0.0:
        while True:
            qty_str = input("How many cups would you like? ")
            try:
                quantity = int(qty_str)
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Please enter a whole number (e.g. 2).")

        order_total = cost * quantity

        # apply the $1 discount when more than one cup of the same drink is ordered
        if quantity > 1:
            print("You get a discount of $1.00 for ordering more than one cup of the same drink!")
            order_total -= 1.00

        print("This order total is: $" + "{:.2f}".format(order_total))
        total_cost += order_total

    # ask if they want more drinks and validate answer
    more_drinks = input("Would you like to have any other drinks? (yes/no): ").strip().lower()
    while more_drinks not in ("yes", "no"):
        more_drinks = input("Please answer 'yes' or 'no': ").strip().lower()

# apply student or general discount to the final total
final_total = total_cost
if is_student:
    student_discount = final_total * 0.10
    final_total -= student_discount
    print(f"As a university student you get 10% off: -${student_discount:.2f}")
else:
    flat_discount = min(1.00, final_total)
    final_total -= flat_discount
    print(f"Non-student discount applied: -${flat_discount:.2f}")

print("Your final total is: $" + "{:.2f}".format(final_total))
print("Thank you, " + customer_name + "! Please come again!")