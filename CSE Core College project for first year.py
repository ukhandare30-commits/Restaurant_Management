GST_RATE = 0.05
def read_menu(file_name):
    items = []
    file = open(file_name, "r")
    for line in file:
        line = line.strip()
        if line != "":
            data = line.split("|")
            dish_name = data[0]
            food_type = data[1]
            price = float(data[2])
            items.append([dish_name, food_type, price])
    file.close()
    return items
def view_menu(file_name, menu_name):
    items = read_menu(file_name)
    print()
    print("18 COMMUNE VIRAT'S RESTAURANT")
    print("          MENU CARD")
    print()
    print("             " + menu_name)
    print()
    print("NO. DISH NAME" + " " * 29 + "TYPE" + " " * 17 + "PRICE")
    print("-" * 71)
    number = 1
    for item in items:
        dish_name = item[0]
        food_type = item[1]
        price = "Rs." + str(int(item[2]))
        number_text = str(number)
        number_space = " " * (4 - len(number_text))
        dish_space = " " * (41 - len(dish_name))
        type_space = " " * (21 - len(food_type))
        price_space = " " * (10 - len(price))
        print(number_text + number_space + dish_name + dish_space + food_type + type_space + price_space + price)
        number = number + 1
    print("-" * 71)
    return items
def add_item(file_name, menu_name):
    print()
    print("ADD ITEM - " + menu_name)
    dish_name = input("Enter dish name: ")
    food_type = input("Enter food type: ")
    try:
        price = float(input("Enter price: "))
    except:
        print("Invalid price.")
        return
    if dish_name == "" or food_type == "":
        print("Dish name and food type cannot be empty.")
        return
    if len(dish_name) > 40:
        print("Dish name cannot be more than 40 characters.")
        return
    if len(food_type) > 20:
        print("Food type cannot be more than 20 characters.")
        return
    if price <= 0:
        print("Price must be greater than 0.")
        return
    file = open(file_name, "a")
    file.write(dish_name + "|" + food_type + "|" + str(price) + "\n")
    file.close()
    print("Item added successfully.")
def modify_item(file_name, menu_name):
    items = read_menu(file_name)
    if len(items) == 0:
        print("No items available.")
        return
    view_menu(file_name, menu_name)
    try:
        number = int(input("Enter item number to modify: "))
    except:
        print("Invalid item number.")
        return
    if number < 1 or number > len(items):
        print("Invalid item number.")
        return
    old_item = items[number - 1]
    print()
    print("Current dish name:", old_item[0])
    print("Current food type:", old_item[1])
    print("Current price:", old_item[2])
    dish_name = input("Enter new dish name: ")
    food_type = input("Enter new food type: ")
    try:
        price = float(input("Enter new price: "))
    except:
        print("Invalid price.")
        return
    if dish_name == "" or food_type == "":
        print("Dish name and food type cannot be empty.")
        return
    if len(dish_name) > 40:
        print("Dish name cannot be more than 40 characters.")
        return
    if len(food_type) > 20:
        print("Food type cannot be more than 20 characters.")
        return
    if price <= 0:
        print("Price must be greater than 0.")
        return
    items[number - 1] = [dish_name, food_type, price]
    file = open(file_name, "w")
    for item in items:
        file.write(item[0] + "|" + item[1] + "|" + str(item[2]) + "\n")
    file.close()
    print("Item modified successfully.")
def delete_item(file_name, menu_name):
    items = read_menu(file_name)
    if len(items) == 0:
        print("No items available.")
        return
    view_menu(file_name, menu_name)
    try:
        number = int(input("Enter item number to delete: "))
    except:
        print("Invalid item number.")
        return
    if number < 1 or number > len(items):
        print("Invalid item number.")
        return
    deleted_item = items[number - 1]
    items.pop(number - 1)
    file = open(file_name, "w")
    for item in items:
        file.write(item[0] + "|" + item[1] + "|" + str(item[2]) + "\n")
    file.close()
    print(deleted_item[0], "deleted successfully.")
def order_item(items, order):
    if len(items) == 0:
        print("No items available.")
        return
    try:
        number = int(input("Enter item number: "))
    except:
        print("Invalid item number.")
        return
    if number < 1 or number > len(items):
        print("Invalid item number.")
        return
    try:
        quantity = int(input("Enter quantity: "))
    except:
        print("Invalid quantity.")
        return
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    selected_item = items[number - 1]
    dish_name = selected_item[0]
    food_type = selected_item[1]
    price = selected_item[2]
    found = False
    for item in order:
        if item[0] == dish_name:
            item[2] = item[2] + quantity
            found = True
            break
    if found == False:
        order.append([dish_name, price, quantity, food_type])
    print(dish_name, "added to your order.")
def view_order(order):
    print()
    print("CURRENT ORDER")
    print("-" * 60)
    if len(order) == 0:
        print("No items in your order.")
        print("-" * 60)
        return
    print("NO. ITEM" + " " * 28 + "QTY" + " " * 8 + "TOTAL")
    print("-" * 60)
    number = 1
    for item in order:
        dish_name = item[0]
        price = item[1]
        quantity = item[2]
        total = price * quantity
        dish_space = " " * (32 - len(dish_name))
        quantity_text = str(quantity)
        quantity_space = " " * (11 - len(quantity_text))
        total_text = "Rs." + str(int(total))
        print(str(number) + "   " + dish_name + dish_space + quantity_text + quantity_space + total_text)
        number = number + 1
    print("-" * 60)
def edit_order(order):
    if len(order) == 0:
        print("Your order is empty.")
        return
    view_order(order)
    try:
        number = int(input("Enter order item number to edit: "))
    except:
        print("Invalid item number.")
        return
    if number < 1 or number > len(order):
        print("Invalid item number.")
        return
    try:
        quantity = int(input("Enter new quantity: "))
    except:
        print("Invalid quantity.")
        return
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return
    order[number - 1][2] = quantity
    print("Quantity updated successfully.")
def remove_order_item(order):
    if len(order) == 0:
        print("Your order is empty.")
        return
    view_order(order)
    try:
        number = int(input("Enter order item number to remove: "))
    except:
        print("Invalid item number.")
        return
    if number < 1 or number > len(order):
        print("Invalid item number.")
        return
    removed_item = order.pop(number - 1)
    print(removed_item[0], "removed from your order.")
def generate_bill(order):
    if len(order) == 0:
        print("No items have been ordered.")
        return
    print()
    print("18 COMMUNE VIRAT'S RESTAURANT")
    print("                 BILL")
    print("-" * 65)
    print("ITEM" + " " * 30 + "QTY" + " " * 8 + "TOTAL")
    print("-" * 65)
    subtotal = 0
    for item in order:
        dish_name = item[0]
        price = item[1]
        quantity = item[2]
        total = price * quantity
        subtotal = subtotal + total
        dish_space = " " * (34 - len(dish_name))
        print(dish_name + dish_space + str(quantity) + " " * 10 + "Rs." + str(int(total)))
    print("-" * 65)
    gst = subtotal * GST_RATE
    grand_total = subtotal + gst
    print("Subtotal:" + " " * 49 + "Rs." + str(round(subtotal, 2)))
    print("GST (5%):" + " " * 48 + "Rs." + str(round(gst, 2)))
    print("Grand Total:" + " " * 45 + "Rs." + str(round(grand_total, 2)))
    print("-" * 65)
    print("Thank you for visiting 18 Commune!")
def owner_menu():
    while True:
        print()
        print("OWNER MENU")
        print("1. Add Item")
        print("2. Modify Item")
        print("3. Delete Item")
        print("4. View Menu")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            print()
            print("Select Menu")
            print("1. Starters")
            print("2. Main Course")
            print("3. Desserts")
            print("4. Drinks")
            print("5. Breads")
            menu_choice = input("Enter your choice: ")
            if menu_choice == "1":
                file_name = "starters.txt"
                menu_name = "STARTERS"
            elif menu_choice == "2":
                file_name = "main_course.txt"
                menu_name = "MAIN COURSE"
            elif menu_choice == "3":
                file_name = "desserts.txt"
                menu_name = "DESSERTS"
            elif menu_choice == "4":
                file_name = "drinks.txt"
                menu_name = "DRINKS"
            elif menu_choice == "5":
                file_name = "breads.txt"
                menu_name = "BREADS"
            else:
                print("Invalid menu choice.")
                continue
            if choice == "1":
                add_item(file_name, menu_name)
            elif choice == "2":
                modify_item(file_name, menu_name)
            elif choice == "3":
                delete_item(file_name, menu_name)
            elif choice == "4":
                view_menu(file_name, menu_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
def customer_menu():
    order = []
    while True:
        print()
        print("WHICH MENU WOULD YOU LIKE TO SEE?")
        print("1. Starters")
        print("2. Main Course")
        print("3. Desserts")
        print("4. Drinks")
        print("5. Breads")
        print("6. Confirm Order")
        choice = input("Enter your choice: ")
        if choice == "6":
            if len(order) == 0:
                print("You have not ordered anything.")
                continue
            print()
            view_order(order)
            confirm = input("Do you want to confirm your order? (y/n): ")
            if confirm.lower() == "y":
                generate_bill(order)
                break
            else:
                continue
        elif choice == "1":
            file_name = "starters.txt"
            menu_name = "STARTERS"
        elif choice == "2":
            file_name = "main_course.txt"
            menu_name = "MAIN COURSE"
        elif choice == "3":
            file_name = "desserts.txt"
            menu_name = "DESSERTS"
        elif choice == "4":
            file_name = "drinks.txt"
            menu_name = "DRINKS"
        elif choice == "5":
            file_name = "breads.txt"
            menu_name = "BREADS"
        else:
            print("Invalid choice.")
            continue
        items = view_menu(file_name, menu_name)
        while True:
            print()
            print("MENU OPTIONS")
            print("1. Order an Item")
            print("2. View Current Order")
            print("3. Edit Current Order")
            print("4. Remove an Item")
            print("5. Change Menu")
            print("6. Confirm Order")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                order_item(items, order)
            elif sub_choice == "2":
                view_order(order)
            elif sub_choice == "3":
                edit_order(order)
            elif sub_choice == "4":
                remove_order_item(order)
            elif sub_choice == "5":
                break
            elif sub_choice == "6":
                if len(order) == 0:
                    print("You have not ordered anything.")
                    continue
                view_order(order)
                confirm = input("Do you want to confirm your order? (y/n): ")
                if confirm.lower() == "y":
                    generate_bill(order)
                    return
            else:
                print("Invalid choice.")
def main():
    while True:
        print()
        print("18 COMMUNE VIRAT'S RESTAURANT")
        print()
        print("1. Owner")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            owner_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice.")
main()