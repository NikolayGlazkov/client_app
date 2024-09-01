from django.urls import path
from .views import *

urlpatterns = [
    path('<int:tag_id>/',by_tag,name='by_tag'),
    path("",index, name='index'),
    path("client_list/",client_list, name='client_list'),
    
    
]
