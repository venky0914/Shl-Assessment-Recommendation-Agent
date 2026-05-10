import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

product_links = [
    "https://www.shl.com/products/product-catalog/view/net-mvc-new/",
    "https://www.shl.com/products/product-catalog/view/net-framework-4-5/",
    "https://www.shl.com/products/product-catalog/view/net-wpf-new/",
    "https://www.shl.com/products/product-catalog/view/net-xaml-new/",
    "https://www.shl.com/products/product-catalog/view/ado-net-new/"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_products = []

for url in product_links:

    print(f"Scraping: {url}")

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    # Extract title
    title_tag = soup.find("h1")

    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        title = "N/A"

    # Extract clean description from meta tag
    description = ""

    meta_desc = soup.find("meta", attrs={"name": "description"})

    if meta_desc:
        description = meta_desc.get("content", "").strip()

    # Store product data
    product = {
        "name": title,
        "url": url,
        "description": description
    }

    all_products.append(product)

    time.sleep(2)

# Create DataFrame
df = pd.DataFrame(all_products)

# Save CSV
df.to_csv("data/shl_catalog.csv", index=False)

print("\nCleaned CSV Saved Successfully!\n")

print(df.head())