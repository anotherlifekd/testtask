from django.urls import path
from .views import create_client, clients, edit_client

app_name = 'account'
urlpatterns = [
    path('create-client', create_client),
    path('edit-client/<id>', edit_client),
    path('clients', clients, name='index')
]
