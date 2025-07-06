from django.db import models


class ServiceCar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.DateField()
    link = models.URLField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'ماشین ها'


class AboutDrive(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام تعمیر کاران')
    about = models.TextField(verbose_name='درباره ')
    image = models.ImageField(upload_to='about', verbose_name='عکس')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'درباره افراد'