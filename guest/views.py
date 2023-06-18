from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import sys
import os
path = os.path.abspath("hotel_database")
sys.path.append(path)
from guest_hotel import Guest
from booking_form_management import  manage_form,manage_form_for_guest
from reservation import  Booking_Form


# Create your views here.
@csrf_exempt 
def handle_accounts(request):
    template = loader.get_template('guest.html')
    context = {}
    phone = request.POST.get("phone")
    name = request.POST.get("name")
    g = Guest.has_register(phone)
    if g is False:
        error_page = loader.get_template('error.html') 
        messages = "can not find your phone number"
        return HttpResponse(error_page.render({'message' : messages},request))
    context,room_id = manage_form_for_guest(phone)
    return HttpResponse(template.render({'data' : context,'name':name},request))

def payment(request):
    template = loader.get_template('payment.html')
    form  = Booking_Form.get(request.POST.get("booking-form-id"))
    bill = form.invoice()
    bill.add()
    context = bill.context()
    return HttpResponse(template.render({'context' : context},request))


