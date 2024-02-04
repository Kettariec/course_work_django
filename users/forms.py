from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from newsletter.forms import StyleFormMixin
from users.models import User


class RegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    """Форма профиля пользователя"""
    class Meta:
        model = User
        fields = ('email', 'password', 'country', 'phone')

    def __init__(self, *args, **kwargs):
        """Скрытие поля password"""
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class ListUserForm(StyleFormMixin, forms.ModelForm):
    """Форма модели User для списка"""
    class Meta:
        model = User
        fields = ('email', 'phone', 'country')
