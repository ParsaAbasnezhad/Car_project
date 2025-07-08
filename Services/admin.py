from django.contrib import admin
from .models import AboutDrive
from .models import Query
from .models import ServiceCar

admin.site.register(AboutDrive)
admin.site.register(Query)


@admin.register(ServiceCar)
class ServiceCarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('status',)
