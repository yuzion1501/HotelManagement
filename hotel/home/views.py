from pipes import Template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def home(request):
    template = loader.get_template('index.html') 
    return HttpResponse(template.render())

def turn_to_home(request):
    return HttpResponseRedirect("/")


@csrf_exempt 
def reservation(request):
    context = {}
    n = request.POST.get("name")
    print(n)
    return HttpResponse('Hello, World!')

