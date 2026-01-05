from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contact_list_and_create(request):
    form = ContactForm()
    contacts = Contact.objects.all()

    return render(request, 'contact_list.html', {
    'form': form, 
    'contacts': contacts
    })