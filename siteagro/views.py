from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from .models import News, Gallery, Goods, Partners

# Create your views here.


def index(request):
    if News.objects.exists():
        ordered_news = News.objects.order_by('-pub_date')
        if ordered_news.__len__() >= 3:
            ordered_news = ordered_news[:3]
        return render(request, "index.html", {'new': ordered_news, 'Index':"current"})
    else:
        ordered_news = None
        return render(request, "index.html", {'new': ordered_news,'Index':"current"})


def detail(request, new_id):
    item = get_object_or_404(News, pk=new_id)
    return render(request, "detail.html", {'item': item})


def gallery(request):
    if Gallery.objects.exists():
        images = Gallery.objects.order_by("pk")
    else:
        images = None
    return render(request, "gallery.html", {"images": images, 'Gallery':"current"})


def prices(request):
    if Goods.objects.exists():
        goods = Goods.objects.order_by("pk")
    else:
        goods = None
    return render(request, "prices.html", {"goods": goods, "Prices":"current"})


def about(request):
    return render(request, "about.html", {"About":"current"})


def contacts(request):  
	return render(request, "contacts.html", {"Contacts":"current"})


def partners(request):
    if Partners.objects.exists():
        images=Partners.objects.order_by("pk")
    else:
        images=None
    return render(request, "partners.html", {"images":images, "Partners":"current"})
