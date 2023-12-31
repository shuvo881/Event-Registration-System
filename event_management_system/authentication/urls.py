from django.urls import path
from .views import SignUpView, SignInView, SignOutView, UserDashboardView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    
    path('dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
]
