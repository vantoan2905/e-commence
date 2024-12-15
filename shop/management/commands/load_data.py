import os
import json
from django.core.management.base import BaseCommand
from shop.models import Product
import tqdm
class Command(BaseCommand):
    help = "Load product data from JSON files in the 'tag' folder"

    def handle(self, *args, **kwargs):
        media_path = os.path.join( "media", "tag")
        print(media_path)
        if not os.path.exists(media_path):
            self.stdout.write(self.style.ERROR(f"Directory {media_path} does not exist."))
            return

        json_files = [f for f in os.listdir(media_path) if f.endswith('.json')]

        if not json_files:
            self.stdout.write(self.style.WARNING("No JSON files found in the 'tag' folder."))
            return

        for json_file in tqdm.tqdm(json_files, desc="Processing JSON files"):
            file_path = os.path.join(media_path, json_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    product = Product(
                        image = json_file.replace('.json', '.jpg'),
                        price=data.get('price', 0.0),
                        articleNumber=data.get('articleNumber', ''),
                        articleType=data.get('articleType', ''),
                        productDisplayName=data.get('productDisplayName', ''),
                        masterCategory=data.get('masterCategory', ''),
                        subCategory=data.get('subCategory', ''),
                        gender=data.get('gender', ''),
                        baseColour=data.get('baseColour', ''),
                        fashionType=data.get('fashionType', ''),
                        season=data.get('season', ''),
                        year=data.get('year', ''),
                        usag=data.get('usage', ''),
                    )
                    product.save()
                except json.JSONDecodeError:
                    self.stdout.write(self.style.ERROR(f"Failed to decode JSON in file {json_file}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error loading product from {json_file}: {e}"))

        self.stdout.write(self.style.SUCCESS("All JSON files processed."))