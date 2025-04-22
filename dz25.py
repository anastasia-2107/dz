class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def __check_value(z):
        if isinstance(z, str) or isinstance(z, int):
            return True
        return False

    @property
    def new_num(self):
        return self.__num

    @new_num.setter
    def new_num(self, num):
        if Account.__check_value(self):
            self.__num = num
        else:
            print("Неверный формат")

    @property
    def new_surname(self):
        return self.__surname

    @new_surname.setter
    def new_surname(self, surname):
        if Account.__check_value(self):
            self.__surname = surname
        else:
            print("Неверный формат")

    @property
    def new_percent(self):
        return self.__percent

    @new_percent.setter
    def new_percent(self, percent):
        if Account.__check_value(self):
            self.__percent = percent
        else:
            print("Неверный формат")

    @property
    def new_value(self):
        return self.__value

    @new_value.setter
    def new_value(self, value):
        if Account.__check_value(self):
            self.__value = value
        else:
            print("Неверный формат")

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)


acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
acc.new_num = 5.80
print(acc.new_num)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()