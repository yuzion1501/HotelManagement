from django.urls import path
from . import views

urlpatterns = [
    path('hotel_manager/', views.login_as_manager, name='a'),
    path('hotel_manager/policy/', views.policy, name='b'),
    path('hotel_manager/handle_form/', views.handle_form, name='b'),
    path('hotel_manager/policy/change_price/', views.change_price, name='b'),
    path('hotel_manager/policy/add_room/', views.add_room, name='b'),
    path('hotel_manager/report/', views.report, name='b'),

]