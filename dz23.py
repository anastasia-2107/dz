class Car:

    def __init__(self, model, year, manufacturer, power, color, price):  # инициализатор
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\n"
              f"Производитель: {self.manufacturer}\nМощность двигателя: {self.power}\n"
              f"Цвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self, model):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self, year):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self, manufacturer):
        return self.manufacturer

    def set_power(self, power):
        self.power = power

    def get_power(self, power):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self, color):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self, price):
        return self.price

h1 = Car("X7 V50i", "2021", "BMW", "530 л.с.", "white", "10790000")
h1.print_info()
