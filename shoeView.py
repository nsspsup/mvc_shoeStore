
class ShoeView:
    @staticmethod
    def display_shoes(shoes):
        if not shoes:
            print("No shoes available.")
        else:
            for shoe in shoes:
                print(shoe)

    @staticmethod
    def display_total_price(price):
        print(f"Total price of all shoes: {price:.2f} EUR")