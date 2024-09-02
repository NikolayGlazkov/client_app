from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import Person,BankAccount,Tag
from .forms import PerForm

class PerCreateView(CreateView):
    template_name = "client_crud/per_create.html"
    form_class = PerForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    

def index(request):
    success_url = reverse_lazy('index')
    return render(request,"client_crud/index.html")

#список клиентов
def client_list(request):
    persons = Person.objects.all()
    tag = Tag.objects.all()
    context = {"persons": persons,"tag":tag}  
    return render(request,"client_crud/client_list.html",context)



# вывод по тегам и тегов
def by_tag(request,tag_id):
    clients = Person.objects.filter(tags=tag_id)
    tags = Tag.objects.all()
    current_tag = Tag.objects.get(pk=tag_id)
    context = {"clients":clients,"tags":tags,"current_tag":current_tag}
    return render(request,'client_crud/by_tag.html', context)


# создание клиента в форме