import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(query):
  """Scrapes product data (image URLs, names, old prices, special prices, and discount percentages)
  for the given search query on Khelmart.com.

  Args:
      query (str): The search query for badminton products.

  Returns:
      pd.DataFrame: A DataFrame containing the scraped product data, or None if scraping fails.
  """

  # Format the query
  formatted_query = query.replace(' ', '+')

  # Define the base URL
  base_url = f'https://www.khelmart.com/catalogsearch/result/index/?product_list_limit=60&q={formatted_query}'

  try:
    response = requests.get(base_url)
    response.raise_for_status()  # Raise an exception for unsuccessful requests
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None  # Indicate scraping failure

  # Parse the response content with BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  # Find all li tags with class 'item product product-item'
  li_tags = soup.find_all('li', {'class': 'item product product-item'})

  # Initialize empty lists to store data
  images = []
  product_names = []
  old_prices = []
  special_prices = []

  # Iterate over each li tag
  for li_tag in li_tags:
    # Extract data (handle potential missing elements)
    img_tag = li_tag.find('img', {'class': 'product-image-photo main-img'})
    img_url = img_tag.get('src') if img_tag else None

    strong_tag = li_tag.find('strong', {'class': 'product name product-item-name'})
    product_name = strong_tag.find('a', {'class': 'product-item-link'}).text.strip() if strong_tag else None

    old_price_tag = li_tag.find('span', {'class': 'old-price'})
    old_price = old_price_tag.find('span', {'class': 'price'}).text.strip().replace('₹', '').replace(',', '') if old_price_tag else None

    special_price_tag = li_tag.find('span', {'class': 'special-price'})
    special_price = special_price_tag.find('span', {'class': 'price'}).text.strip().replace('₹', '').replace(',', '') if special_price_tag else None

    # Append data only if all elements are found (avoid partial data)
    if all([img_url, product_name, old_price, special_price]):
      images.append(img_url)
      product_names.append(product_name)
      old_prices.append(float(old_price))
      special_prices.append(float(special_price))

  # Calculate discount percentages (handle potential division by zero)
  discounts = [
      (old - special) / old * 100 if old > 0 else None
      for old, special in zip(old_prices, special_prices)
  ]

  # Create a DataFrame (ensure all lists have the same length)
  if len(images) == len(product_names) == len(old_prices) == len(special_prices) == len(discounts):
    df = pd.DataFrame({
        'Image': images,
        'Product Name': product_names,
        'Old Price': old_prices,
        'Special Price': special_prices,
        'Discount %': discounts
    })
    return df
  else:
    print("Warning: Inconsistent data lengths. DataFrame not created.")
    return None
