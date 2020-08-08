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
    news = News.objects.all().order_by('-published_date')[:3]
    teams = TeamMember.objects.all()
    galleries = Gallery.objects.all()
    sponsors = Sponsor.objects.all()
    # top_headlines = get_news_headline.delay()
    return render(request, 'index.html', {
        'about': about,
        'news': news,
        'teams': teams,
        'galleries': galleries,
        'sponsors': sponsors,
        # 'top_headlines': top_headlines,
    })


class ContactView(SuccessMessageMixin, CreateView):
    model = ContactInquiry
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')
    success_message = "Query Submitted, we will reach out to you very soon."


def aboutview(request):
    about = About.objects.first()
    galleries = Gallery.objects.all()

    return render(request, 'about.html', {
        'about': about,
        'galleries': galleries,
    })


def newslistview(request):
    news = News.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {
        'news': news,
    })


def newsdetailview(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'blog_details.html', {
        'news': news,
    })