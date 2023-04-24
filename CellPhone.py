class CellPhone:
    brand = None
    model = None
    price = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def toString(self, brand, model, price):
        print(" телефон " +
                "марки= '" + brand + '\'' +
                ", модель = '" + model + '\'' +
                ", цена = " + price)
