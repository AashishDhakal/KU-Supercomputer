from django.urls import path
from .views import ApplicationView

urlpatterns = [
    path('request/', ApplicationView.as_view(), name='application')
]