from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create yogur views here.
def contact_list_and_create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal:contact_list')

    form = ContactForm()
    contacts = Contact.objects.all()

    return render(request, 'contact_list.html', {
    'form': form, 
    'contacts': contacts
    })

def registrarPersonal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        direction = request.POST.get('direction')
    
    Contact.objects.create(name=name, email=email, phone=phone, direction=direction)

    messages.success(request, 'Contacto agregado correctamente')
    return redirect('/')

def editContact(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'edit_contact.html', {'contact': contact})

def updateContact(request, id):
    if request.method == 'POST':        
        contact = Contact.objects.get(id=id)
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.direction = request.POST.get('direction')
        contact.save()
    
    messages.success(request, 'Contacto actualizado correctamente')
    return redirect('/')

def deleteContact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, 'Contacto eliminado correctamente')
    return redirect('/')

