class MainCar:
    def __init__(self, name, model, year, km):
        self.name = name
        self.model = model
        self.year = year
        self.km = km

    def show(self):
        print(f'{self.name}, {self.model}, {self.year}, {self.km}')
