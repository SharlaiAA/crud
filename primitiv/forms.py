from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.forms.EmailField(label = '',
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Электронная почта'}))
    first_name =  forms.forms.EmailField(label = '', max_length = 100,
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
    last_name =  forms.forms.EmailField(label = '', max_length = 100,
        widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-controll'
        self.fields['username'].widget.attrs['placeholder'] = 'Логин'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Необходимо заполнить</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-controll'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Придумайте пароль</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-controll'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Повторите пароль</small></span>' 