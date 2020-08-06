from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import ContactForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


def index(request):
    about = About.objects.first()
    news = News.objects.all().order_by('-published_date')[:3]
    teams = TeamMember.objects.all()
    galleries = Gallery.objects.all()
    sponsors = Sponsor.objects.all()
    return render(request, 'index.html', {
        'about': about,
        'news': news,
        'teams': teams,
        'galleries': galleries,
        'sponsors': sponsors,
    })


class ContactView(SuccessMessageMixin, CreateView):
    model = ContactInquiry
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')
    success_message = "Query Submitted, we will reach out to you very soon."
