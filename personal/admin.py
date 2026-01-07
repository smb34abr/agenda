from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'direction', 'created')
    search_fields = ('name', 'email')
    list_filter = ('created',)
    ordering = ('name',)
    
