from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.turn_to_home, name='home'),
    path('reservation/', views.reservation, name='reservation'),
    path('about/', views.about, name='reservation'),
    path('search/', views.searching, name='search'),    
    path('search/reservation/', views.reservation, name='search'),

]