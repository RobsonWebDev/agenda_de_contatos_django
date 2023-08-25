from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django import forms
from contact.models import Contact
from django.core.paginator import Paginator


class  ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name','last_name', 'phone',

    def clean(self):
        cleaned_data = self.cleaned_data
        
        return super().clean()

def create(request):
    if request.method == 'POST':
        context = {
            'forms': ContactForm(request.POST)
        }

        return render(request, 'contact/create.html', context)

    context = {
        'forms': ContactForm()
    }

    return render(request, 'contact/create.html', context)