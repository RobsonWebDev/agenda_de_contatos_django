from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ...