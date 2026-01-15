import requests
from bs4 import BeautifulSoup
import csv


url = "https://books.toscrape.com/"


response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


products = soup.find_all("article", class_="product_pod")


with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for product in products:
        name = product.h3.a["title"]
        price = product.find("p", class_="price_color").text

        rating_class = product.find("p", class_="star-rating")["class"][1]
        rating = rating_class

        writer.writerow([name, price, rating])

print("✅ Data scraped and saved to products.csv")
