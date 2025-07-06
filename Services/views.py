from django.shortcuts import render
from .models import ServiceCar
from .models import AboutDrive

def about(request):
    drive=AboutDrive.objects.all()
    return render(request, 'services/index.html', {'drive':drive})

def car(request):
    data=ServiceCar.objects.all()
    return render(request,'services/index.html',{'data':data})

