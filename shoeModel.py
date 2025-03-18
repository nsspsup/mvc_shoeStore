# shoe_model.py
class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        if any(s.shoe_id == shoe.shoe_id for s in self.shoes):
            raise ValueError("Shoe with this ID already exists.")
        self.shoes.append(shoe)

    def remove_shoe(self, shoe_id):
        self.shoes = [shoe for shoe in self.shoes if shoe.shoe_id != shoe_id]

    def get_all_shoes(self):
        return self.shoes

    def get_shoes_by_size(self, size):
        return [shoe for shoe in self.shoes if shoe.size == size]

    def get_total_price(self):
        total_price = 0
        for shoe in self.shoes:
            total_price += shoe.price
        return total_price