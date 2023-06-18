from django.urls import path
from . import views

urlpatterns = [
    path('guest/', views.handle_accounts, name='home'),
    path('guest/payment/', views.payment, name='home'),
]