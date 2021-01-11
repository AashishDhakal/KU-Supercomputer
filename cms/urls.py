from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', about_view, name='about'),
    path('news/', news_list_view, name='news_list'),
    path('news/<slug>/', news_detail_view, name='news_detail'),
    path('events/', event_list_view, name='event_list'),
    path('events/<slug>/', event_detail_view, name='event_detail'),
]