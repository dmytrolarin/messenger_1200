from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    '''
    
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Логін"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Пароль"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Підтвердіть пароль"})

class CustomAuthenticationForm(AuthenticationForm):
    '''
    
    '''
    def __init__(self,request, *args, **kwargs):
        super().__init__(request,*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логін'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль'})