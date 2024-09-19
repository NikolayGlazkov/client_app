from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Person,BankAccount,Tag
from .forms import PerForm
from django.utils import timezone
from django.shortcuts import get_object_or_404

class PerCreateView(CreateView):
    template_name = "client_crud/person_create.html"
    form_class = PerForm
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Создание клиента'
        context['tags'] = Tag.objects.all()  # Получите все теги из базы данных
        return context
    
def your_view(request):
    context = {
        'now': timezone.now(),
    }
    return render(request, 'client_crud/basic.html', context)



def index(request):
    context = {
        'page_title': 'Главная',  # Укажите название страницы
    }
    return render(request, "client_crud/index.html", context)


#список клиентов
def client_list(request):
    persons = Person.objects.all()
    tags = Tag.objects.all()  # изменено 'tag' на 'tags'
    context = {"persons": persons, "tags": tags}  
    return render(request, "client_crud/client_list.html", context)




# вывод по тегам и тегов

def by_tag(request, tag_id):
    current_tag = get_object_or_404(Tag, pk=tag_id)
    clients = Person.objects.filter(tags=current_tag)
    tags = Tag.objects.all()
    context = {"clients": clients, "tags": tags, "current_tag": current_tag}
    return render(request, 'client_crud/by_tag.html', context)


# def add_adres
# # создание клиента в форме