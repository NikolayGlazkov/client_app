from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Person,BankAccount,Tag
from .forms import ClientForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.views.generic.edit import UpdateView, DeleteView


class PerCreateView(CreateView):
    template_name = "client_crud/person_create.html"
    form_class = ClientForm
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Создание клиента'
        context['tags'] = Tag.objects.all()  # Получите все теги из базы данных
        return context
    
class ClientUpdateView(UpdateView):
    model = Person
    fields = [
        'name',             # Имя
        'surname',          # Отчество
        'lastname',         # Фамилия
        'date_of_birth',    # Дата рождения
        'place_of_birth',   # Место рождения
        'city',             # Город проживания
        'street',           # Улица
        'post_index',       # Почтовый индекс
        'email',            # Электронная почта
        'phone_number',     # Номер телефона
        'passport_number',  # Номер паспорта
        'passport_seria',   # Серия паспорта
        'issued_by',        # Место выдачи паспорта
        'date_of_issue',    # Дата выдачи паспорта
        'department_code',  # Код подразделения
        'inn_number',       # Номер ИНН
        'snils_number',     # Номер СНИЛС
        'tags'              # Теги
    ]
    template_name = 'client_crud/client_form.html'
    success_url = reverse_lazy('client_list')


# Представление для удаления клиента
class ClientDeleteView(DeleteView):
    model = Person
    template_name = 'client_crud/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')  # После удаления возвращаемся на список клиентов


def client_detail(request, pk):
    client = get_object_or_404(Person, pk=pk)  # Получаем клиента по его первичному ключу (id)
    return render(request, 'client_crud/client_detail.html', {'client': client})



def index(request):
    current_time = datetime.now()
    context = {
        'page_title': 'Главная',
        'current_time': current_time,  # Укажите название страницы
    }
    return render(request, "client_crud/index.html", context)


#список клиентов
def client_list(request):
    persons = Person.objects.all()
    tags = Tag.objects.all()  # изменено 'tag' на 'tags'
    context = {"persons": persons, "tags": tags}  
    return render(request, "client_crud/client_list.html", context)

def client_info(request):
    persons = Person.objects.all()
    context = {"persons": persons, }  
    return render(request, "client_crud/client_info.html", context)

def clients_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)  # Находим тег по его ID
    clients = Person.objects.filter(tags=tag)  # Фильтруем клиентов по этому тегу
    return render(request, 'client_crud/clients_by_tag.html', {'tag': tag, 'clients': clients})