from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.contact_list_and_create, name='contact_list'),
    path('registrarPersonal/', views.registrarPersonal, name='registrarPersonal'),
    path('deleteContact/<int:id>', views.deleteContact, name='deleteContact'),
    path('editContact/<int:id>', views.editContact, name='editContact'),
    path('updateContact/<int:id>', views.updateContact, name='updateContact'),   
]