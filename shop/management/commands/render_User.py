from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from shop.models import Product, SearchHistory, ClickHistory, ViewHistory, Rating
import random
from tqdm import tqdm
import csv

class Command(BaseCommand):
    help = "Populate fake data for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()
        User = get_user_model()

        credentials_file = "user_credentials.csv"
        with open(credentials_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Email", "Password"])

            self.stdout.write("Creating users...")
            users = []
            for _ in tqdm(range(100), desc="Users"):
                plain_password = fake.password()  
                user = User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    password=plain_password,  
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                )
                users.append(user)  
                writer.writerow([user.username, user.email, plain_password])

        self.stdout.write(self.style.SUCCESS(f"User credentials saved to {credentials_file}"))

        self.stdout.write("Creating ratings...")
        for user in tqdm(users, desc="Ratings"):
            for _ in range(random.randint(1, 5)):
                product = Product.objects.order_by('?').first()
                if product:
                    Rating.objects.create(
                        user=user,  
                        product=product,
                        rating=random.randint(1, 5),
                        rating_date=fake.date_time_this_year()  
                    )

        self.stdout.write("Creating view and click history...")
        for user in tqdm(users, desc="View/Click History"):
            for _ in range(random.randint(1, 10)):
                product = Product.objects.order_by('?').first()
                if product:
                    ViewHistory.objects.create(
                        user=user,
                        product=product,
                        view_date=fake.date_time_this_year()
                    )
            for _ in range(random.randint(1, 5)):
                product = Product.objects.order_by('?').first()
                if product:
                    ClickHistory.objects.create(
                        user=user,
                        product=product,
                        click_date=fake.date_time_this_year()
                    )

        search_queries = ['Black', 'Red', 'Tshirts', 'Shorts', 'Pink', 'Sports Shoes']
        self.stdout.write("Creating search history...")
        for user in tqdm(users, desc="Search History"):
            for _ in range(random.randint(1, 5)):
                SearchHistory.objects.create(
                    user=user,
                    query=random.choice(search_queries),
                    search_date=fake.date_time_this_year()
                )

        self.stdout.write(self.style.SUCCESS("Fake data populated successfully!"))
