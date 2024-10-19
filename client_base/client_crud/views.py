from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
from .models import Person, BankAccount, Tag, Contact, Address
from .forms import ClientForm, AddressForm, ContactForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView

from django.views import generic

class PersonListView(generic.ListView):
    model = Person

def client_create(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        address_form = AddressForm(request.POST)
        contact_form = ContactForm(request.POST)
        
        if client_form.is_valid() and address_form.is_valid() and contact_form.is_valid():
            person = client_form.save(commit=False)
            address = address_form.save()
            contact = contact_form.save()
            
            # Связываем адрес и контакты с клиентом
            person.address = address
            person.contact = contact
            person.save()

            return redirect('some_success_url')  # Перенаправление после успешного сохранения
    else:
        client_form = ClientForm()
        address_form = AddressForm()
        contact_form = ContactForm()

    context = {
        'client_form': client_form,
        'address_form': address_form,
        'contact_form': contact_form,
    }

    return render(request, 'client_crud/client_form.html', context)


    
class ClientUpdateView(UpdateView):
    model = Person
    form_class = ClientForm
    template_name = 'client_crud/client_form.html'
    success_url = reverse_lazy('client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm(instance=self.object.contact)
        context['address_form'] = AddressForm(instance=self.object.address)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        contact_form = ContactForm(request.POST, instance=self.object.contact)
        address_form = AddressForm(request.POST, instance=self.object.address)

        if form.is_valid() and contact_form.is_valid() and address_form.is_valid():
            self.object = form.save()
            contact_form.save()
            address_form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# Представление для удаления клиента
class ClientDeleteView(DeleteView):
    model = Person
    template_name = 'client_crud/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')  # После удаления возвращаемся на список клиентов


def client_detail(request, pk):
    client = get_object_or_404(Person, pk=pk)
    contact = get_object_or_404(Contact,pk=pk)  # Получаем клиента по его первичному ключу (id)
    return render(request, 'client_crud/client_detail.html', {'client': client,'contact':contact})



def index(request):
    num_of_person = Person.objects.all().count()

    context = {
        "num_of_person":num_of_person
    }
    return render(request, "client_crud/index.html", context)

    return render(request,"client_crud/index.html")

#список клиентов
def client_list(request):
    # Оптимизация выборки данных
    contact = Contact.objects.all()
    persons = Person.objects.all().prefetch_related('tags')  # Предварительно загружаем теги
    tags = Tag.objects.all()  # Получаем все теги
    
    # Передаем данные в контекст
    context = {
        "persons": persons,
        "tags": tags,
        "contact":contact,
    }  
    
#     context = {
#         "client": men,
#         "bank_accounts": bank_accounts
#     }
#     return render(request, 'client_crud/by_inn.html', context)

def by_tag(request,tag_id):
    clients = Person.objects.filter(tags=tag_id)
    tags = Tag.objects.all()
    current_tag = Tag.objects.get(pk=tag_id)
    context = {"clients":clients,"tags":tags,"current_tag":current_tag}
    return render(request,'client_crud/by_tag.html', context)


