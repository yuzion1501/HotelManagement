import datetime
from datetime import datetime,timedelta
from pipes import Template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import sys
import os
path = os.path.abspath("hotel_database")
sys.path.append(path)
from guest_hotel import Guest
from reservation import Booking_Form
from room import Room
from schedule import create_schedule




# Create your views here.
def home(request):
    template = loader.get_template('index.html') 
    context = Room.select_all_room()
    #return HttpResponse(template.render())
    return HttpResponse(template.render({'data' : context},request))


def turn_to_home(request):
    return HttpResponseRedirect("/")

def check_date(date_of_booking,duration):
    booking_schedule = create_schedule()
    i =0
    while (i < duration):
        temp = date_of_booking + timedelta(days=i)
        if temp in booking_schedule:
            return False
        i = i +1
    return True


@csrf_exempt 
def reservation(request):
    context = {}
    rq = request.POST
    g = Guest(request.POST.get("name"),request.POST.get("email"),request.POST.get("phone"),request.POST.get("id-card"))
    g.add()
    t = datetime.now()
    id = request.POST.get("room-id") + str(t.strftime("%d")) + str(t.strftime("%m")) + str(t.strftime("%Y"))\
        + request.POST.get("id-card")
    status = "pending"
    date_sent = t
    foreigner = "No"

    if len(rq)!=9:
        foreigner = "Yes"
    date_of_booking = datetime.strptime(request.POST.get("date-booking"), "%d/%m/%Y")
    duration = int(request.POST.get("nights-count"))

    if check_date(date_of_booking,duration) is False:
        error_page = loader.get_template('error.html') 
        messages =  "this day was booked"
        return HttpResponse(error_page.render({'message' : messages},request))
    
    if date_of_booking<=date_sent:
        error_page = loader.get_template('error.html') 
        messages = "your booking date must be greater than the current date"
        return HttpResponse(error_page.render({'message' : messages},request))
    form  = Booking_Form(id,request.POST.get("phone"),request.POST.get("room-id"), status,date_of_booking
                         ,date_sent,int(request.POST.get("nights-count")),int(request.POST.get("numbers of guests")),foreigner)
    form.add()
    return HttpResponseRedirect("/")
    #return HttpResponse("okay")

def about(request):
    template = loader.get_template('about.html') 
    return HttpResponse(template.render())



@csrf_exempt 
def searching(request):
    template = loader.get_template('search.html')
    room_type = request.GET.get("room")
    context = Room.select_type_room(room_type)
    
    # context = {
    #     'room' : room_type
    # }
    # return HttpResponse(template.render(context,request))
    return HttpResponse(template.render({'data' : context,'type' : room_type},request))




