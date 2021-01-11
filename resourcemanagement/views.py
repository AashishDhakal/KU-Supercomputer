from django.shortcuts import render
from cms.models import FAQ

# Create your views here.


def request_resource_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'requestresource.html', {'faqs': faqs, })