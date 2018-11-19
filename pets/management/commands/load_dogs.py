from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from pets.models import Dog
from django.core.files import File


def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)


class Command(BaseCommand):
    help = "Load dogs from initial_data/dogs.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting dogs...")
        Dog.objects.all().delete()
        with open(get_path('dogs.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                dog = Dog(
                    name=row['name'],
                    description=row['description'],
                    age=row['age'],
                    size=row['size'],
                    good_with_cats=row['good_with_cats'],
                    good_with_dogs=row['good_with_dogs'],
                    good_with_kids=row['good_with_kids'],
                )
                dog.picture.save(row['image'],
                                 File(open(get_path(row['image']), 'rb')))
                dog.save()
        print(f"{i} dogs loaded!")
