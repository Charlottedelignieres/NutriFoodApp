# myapp/utils.py
import requests

def fetch_products(category, limit):
    url = f"https://world.openfoodfacts.net/api/v2/search?categories_tags_en={category}&limit={limit}&fields=code,product_name,nutrition_grades,categories_tags_en"
    response = requests.get(url)
    
    if response.status_code == 200:
        products_data = response.json()
        return products_data.get('products', [])
    else:
        print(f"Error fetching products for category {category}")
        return []
