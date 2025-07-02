from django.shortcuts import render
from .models import ServiceCar


def car(request):
    data=ServiceCar.objects.all()
    return render(request,'services/index.html',{'data':data})