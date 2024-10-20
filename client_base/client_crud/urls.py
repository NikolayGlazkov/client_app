from django.urls import path
from .views import *

urlpatterns = [
    
    path("",index, name='index'), #главная
    path('contacts/', contacts, name='contacts'), #контакт
    path('about/', about, name='about'), #о нас
    path("client_list/",client_list, name='client_list'), #список клиентов
    path("add/",client_create,name="add"), # Добавить клиента
    path('client/<int:pk>/', client_detail, name='client_detail'),  # Детальная информация о клиенте
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),  # Редактирование клиента
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'), # Удалить клиента
    path('tag/<int:tag_id>/', clients_by_tag, name='clients_by_tag'), # по тегам смотреть
    path('tags/', tag_list, name='tag_list'),  # Список тегов
    path('tags/create/', tag_create, name='tag_create'),  # Создание тега
    path('tags/<int:pk>/edit/', tag_update, name='tag_update'),  # Редактирование тега
    path('tags/<int:pk>/delete/', tag_delete, name='tag_delete'),  # Удаление тега
    path('search/', search_by_inn, name='search_by_inn'),
    
    path('client/<int:pk>/bank_account/create/', BankAccountCreateView.as_view(), name='bank_account_create'),
    path('bankaccount/<int:pk>/', bank_account_detail, name='bankaccount_detail'),
    path('bankaccount/<int:pk>/delete/', BankAccountDeleteView.as_view(), name='bankaccount_delete'),
    path('bankaccount/<int:pk>/update/', BankAccountUpdateView.as_view(), name='bankaccount_update'),
]

