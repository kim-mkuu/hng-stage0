from django.urls import path
from .views import profile_endpoint

urlpatterns = [
    path('me', profile_endpoint, name='profile')
]