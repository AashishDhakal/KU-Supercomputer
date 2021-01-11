from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .forms import ContactForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .tasks import get_news_headline
# Create your views here.


def index(request):
    about = About.objects.first()
    news = News.objects.all().order_by('-published_date')[:5]
    latest_news = news.first()
    news = news[1:]
    teams = TeamMember.objects.all()
    galleries = Gallery.objects.all()
    sponsors = Sponsor.objects.all()
    return render(request, 'index.html', {
        'about': about,
        'news': news,
        'latest_news': latest_news,
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


def about_view(request):
    about = About.objects.first()
    galleries = Gallery.objects.all()

    return render(request, 'about.html', {
        'about': about,
        'galleries': galleries,
    })


def news_list_view(request):
    news = News.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {
        'news': news,
    })


def news_detail_view(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'blog_details.html', {
        'news': news,
    })


def event_list_view(request):
    events = Event.objects.all().order_by('-event_date')
    return render(request, 'event.html', {
        'events': events,
    })


def event_detail_view(request, slug):
    event = get_object_or_404(Event, slug=slug)
    print(event.event_date)
    return render(request, 'eventdetail.html', {
        'event': event,
    })
