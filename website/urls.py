from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('about', views.about, name="about"),
   path('home', views.home, name="home"),
   path('services', views.services, name="services"),
   path('contact', views.contact, name="contact"),
   path('document', views.document, name="document"),
   path('document1', views.document1, name="document1"),
   path('document2', views.document2, name="document2"),
   path('ecommerce', views.ecommerce, name="ecommerce"),
]
