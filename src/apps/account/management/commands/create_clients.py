from django.core.management.base import BaseCommand
from apps.account.models import Client
import names
import random
import phonenumbers
from faker.providers.phone_number.en_US import Provider
from faker import Faker


class CustomPhoneProvider(Provider):
    def phone_number(self):
        while True:
            phone_number = self.numerify(self.random_element(self.formats))
            parsed_number = phonenumbers.parse(phone_number, 'US')
            if phonenumbers.is_valid_number(parsed_number):
                return phonenumbers.format_number(
                    parsed_number,
                    phonenumbers.PhoneNumberFormat.E164
                )

fake = Faker()
fake.add_provider(CustomPhoneProvider)

domains = ["hotmail.com", "gmail.com", "mail.com", "mail.ru", "yahoo.com", "yandex.ru", "ukr.net"]


class Command(BaseCommand):
    help = 'Create clients'

    def handle(self, *args, **options):
        result = []

        for state_name in range(50):
            random_name = names.get_full_name()
            client = Client(client_name=random_name, email=f'{random_name}@{random.choice(domains)}', phone_number=fake.phone_number())
            result.append(client)

        Client.objects.bulk_create(result)
