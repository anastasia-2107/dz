file = "dz21.txt"

f = open(file, "w")
f.write("Первая строка;\nВторая строка;\nТретья строка;\n")
f.close()


f = open(file, "r")
read_line = f.readlines()
print(read_line)
f.close()


first = int(input("Введите номер первой строки, которую хотите заменить: "))
second = int(input("Введите номер второй строки, которую хотите заменить: "))

if 0 <= first < len(read_line) and 0 <= second < len(read_line):
    read_line[first], read_line[second] = read_line[second], read_line[first]
else:
    print("Такой строки нет")

print(read_line)

f = open(file, "w")
f.writelines(read_line)
f.close()