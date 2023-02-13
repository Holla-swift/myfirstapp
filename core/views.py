from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    context = {
        'features': features
    }
    return render(request, 'index.html', context)

def feature_retrieve(request, pk):
    feature = Feature.objects.get(id=pk)
    context = {
        'feature': feature
    }
    return render(request, 'fast.html', context)

