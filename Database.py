starters = ["Tomato Basil Soup|Starter|150\n", "Paneer Tikka|Starter|220\n", "Crispy Corn|Starter|180\n", "Veg Spring Rolls|Starter|200\n", "Hara Bhara Kabab|Starter|190\n", "French Fries|Starter|160\n", "Cheese Balls|Starter|210\n", "Chilli Paneer|Starter|240\n", "Garlic Bread|Starter|170\n", "Peri Peri Fries|Starter|190\n", "Stuffed Mushrooms|Starter|230\n", "Veg Seekh Kebab|Starter|220\n", "Onion Rings|Starter|180\n", "Paneer Pakora|Starter|200\n", "Aloo Tikki|Starter|160\n", "Dahi Ke Kebab|Starter|220\n", "Peanut Masala|Starter|140\n", "Tandoori Momos|Starter|210\n", "Cheese Nachos|Starter|230\n", "Veg Cutlet|Starter|170\n"]
file = open("starters.txt", "w")
file.writelines(starters)
file.close()
main_course = ["Margherita Pizza|Main Course|350\n", "Paneer Butter Masala|Main Course|280\n", "Veg Biryani|Main Course|250\n", "White Sauce Pasta|Main Course|300\n", "Veg Manchurian|Main Course|270\n", "Veg Fried Rice|Main Course|240\n", "Paneer Tikka Masala|Main Course|320\n", "Dal Makhani|Main Course|260\n", "Shahi Paneer|Main Course|300\n", "Mushroom Masala|Main Course|280\n", "Veg Hakka Noodles|Main Course|230\n", "Farmhouse Pizza|Main Course|400\n", "Arrabbiata Pasta|Main Course|290\n", "Malai Kofta|Main Course|310\n", "Kadai Paneer|Main Course|300\n", "Palak Paneer|Main Course|280\n", "Chole Bhature|Main Course|250\n", "Rajma Chawal|Main Course|220\n", "Veg Lasagna|Main Course|320\n", "Stuffed Capsicum|Main Course|290\n"]
file = open("main_course.txt", "w")
file.writelines(main_course)
file.close()
desserts = ["Gulab Jamun|Dessert|100\n", "Brownie|Dessert|150\n", "Ice Cream|Dessert|120\n", "Cheesecake|Dessert|180\n", "Chocolate Mousse|Dessert|160\n", "Fruit Custard|Dessert|130\n", "Chocolate Lava Cake|Dessert|190\n", "Rasmalai|Dessert|140\n", "Kulfi|Dessert|110\n", "Apple Pie|Dessert|170\n", "Caramel Pudding|Dessert|150\n", "Sizzling Brownie|Dessert|220\n", "Rasgulla|Dessert|120\n", "Jalebi|Dessert|100\n", "Tiramisu|Dessert|200\n", "Red Velvet Cake|Dessert|190\n", "Chocolate Donut|Dessert|130\n", "Kesar Pista Kulfi|Dessert|140\n", "Shahi Tukda|Dessert|160\n", "Mango Cheesecake|Dessert|200\n"]
file = open("desserts.txt", "w")
file.writelines(desserts)
file.close()
drinks = ["Fresh Lime Soda|Drink|100\n", "Cold Coffee|Drink|150\n", "Mango Shake|Drink|160\n", "Coca Cola|Drink|80\n", "Masala Chaas|Drink|90\n", "Chocolate Shake|Drink|170\n", "Oreo Shake|Drink|190\n", "Strawberry Shake|Drink|160\n", "Virgin Mojito|Drink|140\n", "Iced Tea|Drink|120\n", "Lemonade|Drink|100\n", "Watermelon Juice|Drink|130\n", "Hot Coffee|Drink|90\n", "Hot Chocolate|Drink|150\n", "Pineapple Juice|Drink|140\n", "Orange Juice|Drink|130\n", "Blue Lagoon|Drink|160\n", "Vanilla Shake|Drink|150\n", "Green Apple Mojito|Drink|170\n", "Cold Chocolate|Drink|160\n"]
file = open("drinks.txt", "w")
file.writelines(drinks)
file.close()
breads = ["Butter Naan|Bread|60\n", "Garlic Naan|Bread|80\n", "Tandoori Roti|Bread|40\n", "Cheese Naan|Bread|100\n", "Lachha Paratha|Bread|90\n", "Missi Roti|Bread|70\n", "Plain Naan|Bread|50\n", "Butter Roti|Bread|45\n", "Stuffed Kulcha|Bread|110\n", "Aloo Paratha|Bread|100\n", "Paneer Paratha|Bread|130\n", "Roomali Roti|Bread|60\n", "Onion Kulcha|Bread|100\n", "Amritsari Kulcha|Bread|120\n", "Pudina Paratha|Bread|90\n", "Methi Paratha|Bread|85\n", "Cheese Garlic Naan|Bread|120\n", "Tandoori Paratha|Bread|100\n", "Peshawari Naan|Bread|130\n", "Ajwain Roti|Bread|55\n"]
file = open("breads.txt", "w")
file.writelines(breads)
file.close()
print("Menu files created successfully.")