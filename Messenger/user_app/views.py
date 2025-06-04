from django.views.generic.edit import CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class RegisterView(CreateView):
    '''
        Створюємо клас відображення сторінки реєстрації, успадковуючи CreateView, для того щоб при заповнені форми створювався об'єкт моделі.
    '''
    # Вказуємо форму, що буде створювати об'єкт
    form_class = CustomUserCreationForm
    # Вказуємо шаблон для відображення
    template_name = 'user_app/register.html'
    # Вказуємо шлях для редіректу після успішного заповнення форми
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    '''
        Створюємо клас відображення сторінки логіну, успадковуючи LoginView, для того щоб при заповнені форми був авторизован користувач.
    '''
    # Вказуємо форму, що буде авторизовувати користувача
    form_class = CustomAuthenticationForm
    # Вказуємо шаблон для відображення
    template_name = 'user_app/login.html'


class CustomLogoutView(LogoutView):
    '''
        Створюємо клас відображення для виходу з акаунту.
    '''
    # Вказуємо на яку сторінку перейти після логауту
    next_page = 'login'