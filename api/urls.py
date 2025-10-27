from django.urls import path
from .views import profile_endpoint, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('me', profile_endpoint, name='profile')
]