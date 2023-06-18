from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import sys
import os
path = os.path.abspath("hotel_database")
sys.path.append(path)
from booking_form_management import  manage_form
from room import Room


# Create your views here.

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