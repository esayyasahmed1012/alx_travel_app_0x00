# listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of listings to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']

        # Create a test user if not exists
        try:
            host = User.objects.get(username='test_host')
        except User.DoesNotExist:
            host = User.objects.create_user(
                username='test_host',
                email='host@example.com',
                password='password123'
            )

        locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret']

        self.stdout.write('Seeding database with {} listings...'.format(count))
        
        for _ in range(count):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                location=random.choice(locations),
                price_per_night=Decimal(str(round(random.uniform(20.0, 200.0), 2))),
                host=host,
                is_available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded {} listings'.format(count)))