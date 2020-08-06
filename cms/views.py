from django.shortcuts import render, HttpResponse
from .models import *

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