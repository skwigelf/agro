from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from .models import News

# Create your views here.


def index(request):
    if News.objects.exists():
        ordered_news = News.objects.order_by('-pub_date')
        if ordered_news.__len__() >= 3:
            ordered_news = ordered_news[:3]
        return render(request, "index.html", {'new': ordered_news})
    else:
        ordered_news = None
        return render(request, "index.html", {'new': ordered_news})


def gallery(request):
    return render(request, "gallery.html", {})


def about(request):
    return render(request, "about.html", {})


def contacts(request):
	return render(request, "contacts.html", {})


def partners(request):
	return render(request, "partners.html", {})
