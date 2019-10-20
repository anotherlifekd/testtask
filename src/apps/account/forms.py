from django.forms import ModelForm
from .models import Client, Address


class CreateClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class EditClientForm(ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class EditAddressForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
