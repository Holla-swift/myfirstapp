from django.urls import path
from . import views
from .views import feature_retrieve, feature_create

urlpatterns = [
    path('', views.index, name='index'),
    path('landing/<pk>', feature_retrieve),
    path('add-feature', feature_create),
]