from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render,redirect
from .models import Person, BankAccount, Tag, Contact, Address
from .forms import ClientForm, AddressForm, ContactForm, TagForm, BankAccountForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView

from django.views import generic


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

            return redirect('client_crud/client_detail.html')  # Перенаправление после успешного сохранения
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
        context['contact_form'] = ContactForm(instance=self.object.contacts)
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
    person = get_object_or_404(Person, pk=pk)
    contact = get_object_or_404(Contact, pk=pk)
    bankak = BankAccount.objects.filter(person=person)  # Получаем все счета клиента
    
    return render(request, 'client_crud/client_detail.html', {'person': person, 'contact': contact, 'bankak': bankak,})


def index(request):
    num_of_person = Person.objects.all().count()

    context = {
        "num_of_person":num_of_person
    }
    return render(request, "client_crud/index.html", context)

# контакты
def contacts(request):
    context = {
        'page_title': 'контакты',
    }
    return render(request, "client_crud/contacts.html", context)


# о нас
def about(request):
    context = {
        'page_title': 'о нас',
    }
    return render(request, "client_crud/about.html", context)

#список клиентов
def client_list(request):
    persons = Person.objects.all().prefetch_related('contacts', 'tags')  # Предварительно загружаем теги и контакты
    
    tags = Tag.objects.all()  # Получаем все теги
    
    # Передаем данные в контекст
    context = {
        "persons": persons,
        "tags": tags,
       
    }  
    
    return render(request, "client_crud/client_list.html", context)


def clients_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)  # Находим тег по его ID
    person = Person.objects.filter(tags=tag)  # Фильтруем клиентов по этому тегу
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'client_crud/clients_by_tag.html', {'tag': tag, 'person': person,'contact':contact})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'client_crud/tag_list.html', {'tags': tags})


# Создание нового тега
def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'client_crud/tag_form.html', {'form': form})

# Редактирование существующего тега
def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'client_crud/tag_form.html', {'form': form})

# Удаление тега
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')
    return render(request, 'client_crud/tag_confirm_delete.html', {'tag': tag})


def search_by_inn(request):
    if request.method == 'POST':
        inn_number = request.POST.get('inn_number')
        if inn_number:
            # Поиск клиента по ИНН
            person = Person.objects.filter(inn_number=inn_number).first()
            if person:
                # Перенаправляем на страницу с информацией о клиенте
                return redirect('client_detail', pk=person.pk)
            else:
                # Если клиент не найден, отображаем сообщение об ошибке на странице списка клиентов
                persons = Person.objects.all()  # Получаем список всех клиентов для отображения
                tags = Tag.objects.all()  # Получаем все теги для отображения
                context = {
                    'error': "Клиент не найден.",
                    'persons': persons,
                    'tags': tags,
                }
                return render(request, 'client_crud/client_list.html', context)
        else:
            # Если ИНН не был введен, показываем сообщение об ошибке
            persons = Person.objects.all()
            tags = Tag.objects.all()
            context = {
                'error': "Введите ИНН для поиска.",
                'persons': persons,
                'tags': tags,
            }
            return render(request, 'client_crud/client_list.html', context)

    # Если не POST-запрос, просто редиректим на страницу списка клиентов
    return redirect('client_list')

  



class BankAccountCreateView(CreateView):
    model = BankAccount
    form_class = BankAccountForm
    template_name = 'client_crud/bank_account_form.html'
    success_url = reverse_lazy('client_list')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        person_pk = self.kwargs.get('pk')  # Получите pk клиента из URL
        kwargs['instance'] = BankAccount(person=get_object_or_404(Person, pk=person_pk)) 
        return kwargs
    def form_valid(self, form):
        # Получите pk клиента из URL
        person_pk = self.kwargs.get('pk')
        # Создайте банковский счет, связав его с клиентом
        form.instance.person = get_object_or_404(Person, pk=person_pk)
        return super().form_valid(form)
    

def bank_account_detail(request, pk):
    bank_account = get_object_or_404(BankAccount, pk=pk)
    context = {'bank_account': bank_account}
    return render(request, 'client_crud/bank_account_detail.html', context)