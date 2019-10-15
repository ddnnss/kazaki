from django.shortcuts import render
from .models import *

def index(request):
    indexActive = True
    images = GalleryImage.objects.filter(showIndex=True)
    news = News.objects.filter()
    events = Event.objects.all()[:3]
    return render(request, 'index.html', locals())

def news(request):
    newsActive = True
    news = News.objects.all()
    return render(request, 'news.html', locals())

def newsItem(request, slug):
    newsActive = True
    news_item = News.objects.get(name_slug=slug)

    return render(request, 'news-item.html', locals())
def events(request):
    eventsActive = True
    return render(request, 'event-item.html', locals())

def about(request):
    aboutActive = True
    return render(request, 'index.html', locals())

def contacts(request):
    contactsActive = True
    return render(request, 'contacts.html', locals())

def ataman(request):
    atamanActive = True
    return render(request, 'index.html', locals())