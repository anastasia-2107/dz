s = input("Введите строку: ")
# I am learning Python. hello WORLD!
one = s[: s.find("h") + 1]
two = s[s.find("h") + 1:s.rfind("h")]
three = s[s.rfind("h"):]
# print(one)
# print(two)
# print(three)
print(one + (two[::-1]) + three)


