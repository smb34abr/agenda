from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
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