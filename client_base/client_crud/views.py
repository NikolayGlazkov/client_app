from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Person,BankAccount,Tag


def index(request):

    return render(request,"client_crud/index.html")

#список клиентов
def client_list(request):
    persons = Person.objects.all()
    tag = Tag.objects.all()
    context = {"persons": persons,"tag":tag}  
    return render(request,"client_crud/client_list.html",context)

# def by_inn(request, inn_number):
#     # Фильтруем клиентов по ИНН
#     men = Person.objects.filter(inn_number=inn_number)
    
#     # Получаем все счета, связанные с этим клиентом
#     bank_accounts = BankAccount.objects.filter(person__inn_number=inn_number)
    
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


