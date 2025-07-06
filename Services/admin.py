from django.contrib import admin
from .models import ServiceCar
from .models import AboutDrive
admin.site.register(AboutDrive)



@admin.register(ServiceCar)
class ServiceCarAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name',)
    list_filter = ('status',)




