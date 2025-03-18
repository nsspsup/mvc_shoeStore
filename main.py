from shoeController import ShoeController


def main():
    controller = ShoeController()

    # Pre-load 10 shoes
    preloaded_shoes = [
        (1, 42, 120.0, "Men", "Sneakers", "Black", "Nike"),
        (2, 38, 90.0, "Women", "Sandals", "White", "Adidas"),
        (3, 40, 150.0, "Unisex", "Running Shoes", "Blue", "Puma"),
        (4, 44, 110.0, "Men", "Boots", "Brown", "Timberland"),
        (5, 36, 85.0, "Women", "Flats", "Red", "Gucci"),
        (6, 41, 130.0, "Unisex", "Trainers", "Green", "Reebok"),
        (7, 39, 95.0, "Women", "Heels", "Pink", "Louis Vuitton"),
        (8, 45, 140.0, "Men", "Loafers", "Tan", "Clarks"),
        (9, 37, 100.0, "Women", "Sneakers", "Yellow", "New Balance"),
        (10, 43, 125.0, "Unisex", "Casual Shoes", "Grey", "Skechers")
    ]

    for shoe in preloaded_shoes:
        controller.add_shoe(*shoe)

    while True:
        print("\n1. Add Shoe")
        print("2. Remove Shoe")
        print("3. Show All Shoes")
        print("4. Show Shoes by Size")
        print("5. Show Total Price")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                shoe_id = int(input("Enter Shoe ID: "))
                size = int(input("Enter Shoe Size: "))
                price = float(input("Enter Shoe Price: "))
                gender = input("Enter Shoe Gender (Men/Women/Unisex): ")
                shoe_type = input("Enter Shoe Type (Sneakers, Sandals, etc.): ")
                color = input("Enter Shoe Color: ")
                brand = input("Enter Shoe Brand: ")
                controller.add_shoe(shoe_id, size, price, gender, shoe_type, color, brand)
            except ValueError:
                print("Invalid input, please enter correct values.")

        elif choice == "2":
            try:
                shoe_id = int(input("Enter Shoe ID to remove: "))
                controller.remove_shoe(shoe_id)
            except ValueError:
                print("Invalid input, please enter a valid ID.")

        elif choice == "3":
            controller.show_all_shoes()

        elif choice == "4":
            try:
                size = int(input("Enter Shoe Size: "))
                controller.show_shoes_by_size(size)
            except ValueError:
                print("Invalid input, please enter a valid size.")

        elif choice == "5":
            controller.show_total_price()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
