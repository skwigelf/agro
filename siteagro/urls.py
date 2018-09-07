from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('partners', views.partners, name='partners'),
    path('gallery', views.gallery, name="gallery"),
    path('prices', views.prices, name="prices"),
    path('<int:new_id>/', views.detail, name='detail'),
]
