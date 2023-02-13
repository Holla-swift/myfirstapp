from django.urls import path
from . import views
from .views import feature_retrieve

urlpatterns = [
    path('', views.index, name='index'),
    path('landing/<pk>', feature_retrieve)
]