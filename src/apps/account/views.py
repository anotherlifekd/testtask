from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Client, Address
from .forms import CreateClientForm, EditClientForm, EditAddressForm


def clients(request):
    clients = Client.objects.all().order_by('client_name')

    if request.GET.get('search') or request.GET.get('sort_by'):
        search_term = request.GET.get('search') or ''
        sort_term = request.GET.get('sort_by') or 'client_name'

        clients = clients.filter(
            Q(client_name__icontains=search_term) |
            Q(phone_number__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(address__suburb__icontains=search_term)
        ).order_by(sort_term).distinct()

    paginator = Paginator(clients, 5)
    page = request.GET.get('page')
    clients = paginator.get_page(page)
    context = {
        'clients': clients,
        'search_value': request.GET.get('search') if request.GET.get('search') else '',
        'sort_value': request.GET.get('sort_by') if request.GET.get('sort_by') else 'client_name'
    }

    return render(request, 'account/index.html', context=context)


def create_client(request):

    if request.method == "GET":
        form = CreateClientForm
    elif request.method == "POST":
        form = EditClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:index'))

    return render(request, 'account/create-client.html', {'form': form})


def edit_client(request, id):
    client = Client.objects.get(id=id)
    AddressInlineFormSet = inlineformset_factory(
        Client, Address,
        fields=('contact_name', 'street', 'suburb', 'state', 'zip_code'),
        form=EditAddressForm,
        can_delete=True,
        extra=1)

    if request.method == "GET":
        client_form = EditClientForm(instance=client)
        formset = AddressInlineFormSet(instance=client)
    elif request.method == "POST":
        client_form = EditClientForm(request.POST, instance=client)
        formset = AddressInlineFormSet(request.POST, instance=client)
        if client_form.is_valid() and formset.is_valid():
            client_form.save()
            formset.save()
            return redirect(reverse('account:index'))

    context = {'client': client, 'client_form': client_form, 'address_form': formset}
    return render(request, 'account/edit-client.html', context=context)
