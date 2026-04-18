from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('main', views.prompt, name='main'),
    path('output', views.generated, name='generate'),
]