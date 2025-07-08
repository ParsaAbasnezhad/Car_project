from django.shortcuts import render
from .models import ServiceCar, AboutDrive, Query



def car(request):
    data=ServiceCar.objects.all()
    return render(request,'services/index.html',{'data':data})


def about(request):
    drive=AboutDrive.objects.all()
    return render(request, 'services/index.html', {'drive':drive})



def query_view(request):
    if request.method=='POST':
        location=request.POST.get('location')
        date1=request.POST.get('date1')
        date2=request.POST.get('date2')
        query=Query.objects.create(location=location,date1=date1,date2=date2)
        return render(request,'services/index.html',{'query':query})
    return render(request,'services/index.html')