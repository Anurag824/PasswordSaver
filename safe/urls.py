from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',Signup.as_view(), name='landing'),
    path('login/',Login.as_view(), name='login'),
    path('home/',Safekeeper.as_view(), name='PasswordSafe'),
]