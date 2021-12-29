from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('first_name', 'last_name', 'message')
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control",
                       "type": 'text',
                       "placeholder": "Ваше имя",
                        }),
            "last_name": forms.TextInput(
                attrs={"class": "form-control",
                       "type": 'text',
                       "placeholder": "Ваша фамилия",
                       }),
            "message": forms.TextInput(
                attrs={"class": "form-control",
                       "type": 'text',
                       "placeholder": "Ваш текст",
                       }),

        }