from django.db import models

# Create your models here.

class pisos(models.Model):
    address = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    year_of_construction = models.IntegerField()
    year_of_renovation = models.IntegerField()
    total_prince = models.IntegerField()
    total_area = models.IntegerField()
    price_m = models.IntegerField()
    has_elevator = models.BooleanField()
    valuation_date = models.DateField()

