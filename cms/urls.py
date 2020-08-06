from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', ContactView.as_view(), name='contact')
]