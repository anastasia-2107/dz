d = {
    "John": {
        "N": "3056",
        "S": "8463",
        "E": "8441",
        "W": "2694",
    },
    "Tom": {
        "N": "4832",
        "S": "6786",
        "E": "4737",
        "W": "3612",
    },
    "Anne": {
        "N": "5239",
        "S": "4802",
        "E": "5820",
        "W": "1859",
    },
    "Fiona": {
        "N": "3904",
        "S": "3645",
        "E": "8821",
        "W": "2451",
    }
}

for x in d:
    print(x)
    for i, j in d[x].items():
        print(i, ": ", j)
name = input("Имя: ")
location = input("Регион: ")
print(d[name][location])
new_count = input("Новое значение: ")
d[name][location] = new_count
print(d[name])
