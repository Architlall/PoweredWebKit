from django.urls import path
from . import views

app_name='customer'
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('', views.home, name='home'),
]
