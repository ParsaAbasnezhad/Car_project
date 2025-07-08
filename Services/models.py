from django.db import models


class ServiceCar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services')
    city = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    year = models.DateField(null=True)
    link = models.URLField(null=True)
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


class Query(models.Model):
    map = models.CharField(max_length=100, verbose_name='مکان')
    date = models.DateField(verbose_name='زمان تحویل')
    date_map = models.DateField(verbose_name='زمان اتمام')

    def __str__(self):
        return self.map
