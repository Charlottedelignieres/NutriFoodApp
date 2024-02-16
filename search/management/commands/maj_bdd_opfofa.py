# management/commands/load_products.py
from django.core.management.base import BaseCommand
from search.utils import fetch_products
from search.models import Product

class Command(BaseCommand):
    help = 'Load products from API into the database'

    def handle(self, *args, **options):
        categories = ["Meats", "Desserts", "Cheeses", "Frozen foods", "Yogurts"]
        max_products_per_category = 100
        total_products_loaded = 0

        for category in categories:
            products = fetch_products(category, max_products_per_category)
            num_products = len(products)
            total_products_loaded += num_products

            for product_data in products:
                try:
                    # Créer un produit dans la base de données
                    Product.objects.create(
                        code=product_data.get('code'),
                        product_name=product_data.get('product_name'),
                        nutrition_grade=product_data.get('nutrition_grades'),
                        category=category
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed to create product: {e}'))

            self.stdout.write(self.style.SUCCESS(f'{num_products} products loaded for category {category}'))

        self.stdout.write(self.style.SUCCESS(f'Total {total_products_loaded} products loaded from API'))
