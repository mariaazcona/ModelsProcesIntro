from django.core.management.base import BaseCommand
from myapp.models import Item


class Command(BaseCommand):
    help = 'Delete all items on database'

    def handle(self, *args, **kwargs):
        Item.objects.all().delete()
