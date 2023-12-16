from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255, required=True)
    second_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    locate = forms.CharField(max_length=255, required=True)
    birthday = forms.DateField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'second_name', 'last_name', 'email', 'locate',
                  'birthday']

class MyLoginForm(AuthenticationForm):
    class Meta:
        model = User  # Укажите вашу модель пользователя, например, Client
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'your-class'})  # Замените 'your-class' на ваш класс для стилей
        self.fields['password'].widget.attrs.update({'class': 'your-class'})

class NameForm(forms.Form):
    good_id = forms.IntegerField(label="Good id")
    prod_cnt = forms.IntegerField(label="Count")



class GoodForm(forms.Form):
    good_name = forms.CharField(label="Good name")
    short_info =forms.CharField(label="Short info")
    good_price = forms.FloatField(label="Good price")

class StorageForm(forms.Form):
    locate = forms.CharField(label='locate')
    worktime = forms.CharField(label='worktime')