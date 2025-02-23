from django.core.management.base import BaseCommand
import json
from myapp.models import Item
from decimal import Decimal


class Command(BaseCommand):
    help = "Import products from JSON file"

    def handle(self, *args, **kwargs):
        with open("myapp/data/products.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            Item.objects.create(
                name=item["title"],
                price=Decimal(item.get('price', 0)),
                description=item.get("description", "")
            )
