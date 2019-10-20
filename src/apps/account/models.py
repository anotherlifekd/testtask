from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    client_name = models.CharField(max_length=64, blank=True, unique=True, db_index=True)
    email = models.EmailField(blank=True, db_index=True)
    phone_number = PhoneNumberField(blank=True)

    def __str__(self):
        return self.client_name


class State(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Address(models.Model):  # A client can have multiple addresses
    contact_name = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    suburb = models.CharField(max_length=128, db_index=True, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='clientaddress')

    def __str__(self):
        return 'Address'
