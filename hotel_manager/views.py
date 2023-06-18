import datetime
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import sys
import os
path = os.path.abspath("hotel_database")
sys.path.append(path)
from booking_form_management import  manage_form
from reservation import Booking_Form
from room import Room
from data import get_data_report






# Create your views here.
@csrf_exempt 
def login_as_manager(request):
    if request.method == 'POST':
        try :
            user = authenticate( username=request.POST.get("admin-id"),password=request.POST.get("password"))  
            login(request, user)
            if user is None :
                error_page = loader.get_template('error.html') 
                messages = "can not find this admin-user"
                return HttpResponse(error_page.render({'message' : messages},request))
        except :
            error_page = loader.get_template('error.html') 
            messages = "can not find this admin-user"
            return HttpResponse(error_page.render({'message' : messages},request))
    return management(request)

@csrf_exempt 
@login_required
def management(request):
    template = loader.get_template('hotel_manager.html')
    context = manage_form("pending")
    name  = request.POST.get("admin-id")
    return HttpResponse(template.render({'data' : context,'name':name},request))
    


def payment(request):
    return HttpResponse("this is a payment site")

@csrf_exempt 
@login_required
def handle_form(request):
    form = Booking_Form.get(request.POST.get("booking-form-id"))
    if request.POST.get("accept") == "Yes":
        Booking_Form.delete(request.POST.get("booking-form-id"))
        form.change_status("accept")
        form.add()
    else:
        Booking_Form.delete(request.POST.get("booking-form-id"))
        form.change_status("reject")
        form.add()

    # template = loader.get_template('hotel_manager.html')
    # context = manage_form("pending")
    # name  = request.POST.get("admin-id")
    # return HttpResponse(template.render({'data' : context,'name':name},request))
    return HttpResponseRedirect("/hotel_manager/")


@login_required
def policy(request):
    template = loader.get_template('policy.html')
    return HttpResponse(template.render())

@csrf_exempt 
def change_price(request):
    if request.POST.get("Room-A-changing") != "":
        price = int(request.POST.get("Room-A-changing"))
        Room.change_price_room("A",price)

    if request.POST.get("Room-B-changing") != "":
        price = int(request.POST.get("Room-B-changing"))
        Room.change_price_room("B",price)

    if request.POST.get("Room-C-changing") != "":
        price = int(request.POST.get("Room-C-changing"))
        Room.change_price_room("C",price)

    return HttpResponseRedirect("/hotel_manager/")

@csrf_exempt 
def add_room(request):
    R = Room(request.POST.get("ID"),request.POST.get("Type"),request.POST.get("Price"),request.POST.get("Available"))
    R.add()
    return HttpResponseRedirect("/hotel_manager/")

# def add_room(request):
#     R = Room(request.POST.get("ID"),request.POST.get("Type"),request.POST.get("Price"),request.POST.get("Available"))
#     template = loader.get_template('report.html')
#     return HttpResponse(template.render())


def report(request):
    data = get_data_report()
    template = loader.get_template('report.html')
    return HttpResponse(template.render({'data' : data,},request))










