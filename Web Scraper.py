import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com"  # Replace with target website URL

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    # Example selectors (change according to website structure)
    titles = soup.find_all("h2")
    prices = soup.find_all("span", class_="price")

    for title, price in zip(titles, prices):
        product = {
            "title": title.text.strip(),
            "price": price.text.strip()
        }
        products.append(product)

    # Save to CSV
    with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "price"])
        writer.writeheader()
        writer.writerows(products)

    print("Data scraped and saved successfully!")

else:
    print("Failed to fetch website")