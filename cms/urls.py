from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', aboutview, name='about'),
    path('news/', newslistview, name='newslist'),
    path('news/<slug>/', newsdetailview, name='newsdetail'),
]