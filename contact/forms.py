from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Escreva aqui',
            }
        
        ),
        label = 'Primeiro Nome',
        help_text = 'Texto de ajuda para o usuário',
    )

    class Meta:
        model = models.Contact
        fields = 'first_name','last_name', 'phone',

    def clean(self):
        
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de error', code = 'invalid'
            )
        )

        return super().clean()
