from django.shortcuts import render

def index(request):
    indexActive = True
    return render(request, 'index.html', locals())

def news(request):
    newsActive = True
    return render(request, 'news.html', locals())

def newsItem(request):
    newsActive = True
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