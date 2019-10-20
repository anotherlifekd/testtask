from django.contrib import admin
from .models import (
    Client, Address, State
)


class ClientAdressAdmin(admin.TabularInline):
    model = Address
    extra = 1
    list_display = ['contact_name', 'street', 'suburb', 'state', 'zip_code', 'client']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'email', 'phone_number']
    inlines = [ClientAdressAdmin]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
