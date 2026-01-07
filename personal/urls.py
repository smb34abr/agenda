from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.contact_list_and_create, name='contact_list'),
    path('registrarPersonal/', views.registrarPersonal, name='registrarPersonal'),
]