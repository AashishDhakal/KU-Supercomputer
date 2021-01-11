from django.urls import path
from .views import request_resource_view

urlpatterns = [
    path('request/', request_resource_view, name='application')
]