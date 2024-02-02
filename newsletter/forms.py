from django import forms
from newsletter.models import Client, NewsLetter, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('user',)


class NewsLetterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = NewsLetter
        exclude = ('user', 'status',)
        widgets = {
            'time': forms.TimeInput(
                attrs={'type': 'time', }
            ),
            'date': forms.DateInput(
                attrs={'type': 'date', }
            )
        }
