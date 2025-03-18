# shoe_controller.py
from shoe import Shoe
from shoeModel import ShoeModel
from shoeView import ShoeView

class ShoeController:
    def __init__(self):
        self.model = ShoeModel()
        self.view = ShoeView()

    def add_shoe(self, shoe_id, size, price, gender, shoe_type, color, brand):
        try:
            shoe = Shoe(shoe_id, size, price, gender, shoe_type, color, brand)
            self.model.add_shoe(shoe)
            print("Shoe added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_shoe(self, shoe_id):
        self.model.remove_shoe(shoe_id)
        print("Shoe removed successfully!")

    def show_all_shoes(self):
        shoes = self.model.get_all_shoes()
        self.view.display_shoes(shoes)

    def show_shoes_by_size(self, size):
        shoes = self.model.get_shoes_by_size(size)
        self.view.display_shoes(shoes)

    def show_total_price(self):
        total_price = self.model.get_total_price()
        self.view.display_total_price(total_price)