from django.urls import path
from .views import *

urlpatterns = [
    # path('<int:tag_id>/',by_tag,name='by_tag'),
    path("",index, name='index'),
    path("client_list/",client_list, name='client_list'),
    path("client_info/",client_info, name='client_info'),
    path("add",PerCreateView.as_view(),name="add"),
    path('client/<int:pk>/', client_detail, name='client_detail'),  # Детальная информация о клиенте
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),  # Редактирование клиента
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('clients/tag/<int:tag_id>/', clients_by_tag, name='clients_by_tag'),
    
]
