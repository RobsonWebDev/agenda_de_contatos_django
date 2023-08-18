from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name',
    list_editable = 'show',
    list_per_page = 10
    list_max_show_all = 100

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = '-id',