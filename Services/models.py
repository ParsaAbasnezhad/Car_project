from django.db import models


class ServiceCar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    year = models.DateField()
    price = models.IntegerField()
    link = models.URLField()
    def __str__(self):
        return self.name + ' ' + str(self.price)

