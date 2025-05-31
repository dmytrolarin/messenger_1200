from django.views.generic.edit import CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(CreateView):
    '''
    
    '''
    #
    form_class = CustomUserCreationForm
    #
    template_name = 'user_app/register.html'
    #
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    '''
    
    '''
    #
    form_class = CustomAuthenticationForm
    #
    template_name = 'user_app/login.html'


class CustomLogoutView(LogoutView):
    '''
    
    '''
    #
    next_page = 'login'