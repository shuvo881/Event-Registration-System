from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from events.models import Registration

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class SignInView(LoginView):
    template_name = 'login.html'


class SignOutView(LogoutView):
    next_page = '/'  # Redirect to the home page after logout
    
    

class UserDashboardView(TemplateView):
    template_name = 'dashboard.html'

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_registrations = Registration.objects.filter(user=self.request.user)
        context['user_registrations'] = user_registrations
        return context"""

