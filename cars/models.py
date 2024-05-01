from django.db import models


class Car(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=30)
    engine = models.FloatField()
