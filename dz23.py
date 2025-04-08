class Car:
    model = "model"
    year = "0000"
    manufacturer = "manufacturer"
    power = "power"
    color = "color"
    price = "0000000"

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

    # def set_name(self, model, year, manufacturer, power, color, price):  # устанавливаем новое имя
    #     self.model = model
    #     self.year = year
    #     self.manufacturer = manufacturer
    #     self.power = power
    #     self.color = color
    #     self.price = price

    # def get_name(self):  # получаем имя
    #     self.model = model
    #     self.year = year
    #     self.manufacturer = manufacturer
    #     self.power = power
    #     self.color = color
    #     self.price = price


h1 = Car()
h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())