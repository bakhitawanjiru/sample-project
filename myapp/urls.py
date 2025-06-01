from django.urls import path

from . import views 


urlpatterns = [
path('',views.welcome, name="welcome"),
path('home/',views.home, name="home"),
path('about/',views.about, name="about"),
path('contact/',views.contact, name="contact"),
path('blogs/',views.display_blogs, name="display_blogs")
]
