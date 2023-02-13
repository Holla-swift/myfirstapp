from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def landing(request):
    return render(request, 'landing.html')

def generic(request):
    return render(request, 'generic.html')

def elements(request):
    return render(request, 'elements.html')
