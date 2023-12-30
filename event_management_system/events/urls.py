from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.api_views import EventViewSet, RegistrationViewSet
from .views.views import EventListView
router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'registrations', RegistrationViewSet, basename='registration')

urlpatterns = [
    path('api/', include(router.urls)),
    path('',EventListView.as_view(), name='events')
]
