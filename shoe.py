
class Shoe:
    def __init__(self, shoe_id, size, price, gender, shoe_type, color, brand):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.shoe_id = shoe_id
        self.size = size
        self.price = price
        self.gender = gender
        self.shoe_type = shoe_type
        self.color = color
        self.brand = brand

    def __str__(self):
        return (f"ID: {self.shoe_id}, Size: {self.size}, Price: {self.price:.2f} EUR, Gender: {self.gender}, Type: {self.shoe_type}, Color: {self.color}, Brand: {self.brand}")