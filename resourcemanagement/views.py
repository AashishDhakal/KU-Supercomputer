from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ApplicationForm
from .models import Application
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class ApplicationView(SuccessMessageMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application.html'
    success_url = reverse_lazy('application')
    success_message = "Application Submitted, you will be emailed with your credentials once approved."