# views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# views.py
from django.contrib.auth.views import LoginView

class SignInView(LoginView):
    template_name = 'login.html'


# views.py
from django.contrib.auth.views import LogoutView

class SignOutView(LogoutView):
    next_page = '/'  # Redirect to the home page after logout
