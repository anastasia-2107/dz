import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("a", class_="now_sales-jk-el")
    for el in elements:
        name = el.find("h1").text.strip()
        city = el.find("span").text.strip()
        price = el.find("div", class_="now_sale-jk-price").text.strip()
        data = {
            "name": name,
            "city": city,
            "price": price,
            }
        write_csv(data)


def write_csv(data):
    with open("gk_usi.csv", "a", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data["name"], data["city"], data["price"]))


def main():
    url = "https://gk-usi.ru/?ysclid=maz9id4t4m497909724"
    get_data(get_html(url))


if __name__ == '__dz34__':
    main()