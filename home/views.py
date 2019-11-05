from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import Album
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from django.template import loader

def index(reuest):
     template = loader.get_template('home/index.html')
     context = {}
     return HttpResponse(template.render(context,reuest))


def details(request, productId):
     return HttpResponse("<h2>Hey man. this is for product ID " + str(productId)+" </h2>")