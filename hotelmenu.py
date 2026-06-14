menu = {
    'Pizza': 50,
    'Pasta': 40,
    'Burger': 60,
    'Coffee': 80,
    'Salad': 70,
}

# Greet
print("Welcome to Python Restaurant")
print("Pizza: Rs50\nPasta: Rs40\nBurger: Rs60\nCoffee: Rs80\nSalad: Rs70")

order_total = 0

item_1 = input("Enter the name of item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available.")

another_order = input("Do you want to add another item? (yes/no): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of another item: ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available.")

print(f"The total amount to pay is Rs{order_total}")