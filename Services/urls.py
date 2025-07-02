from django.urls import path
from . import views

app_name = 'Services'
urlpatterns = [
    path('', views.car, name='car'),
]
