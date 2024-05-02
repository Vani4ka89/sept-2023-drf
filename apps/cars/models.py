from django.db import models
from core.models import BaseModel


class Car(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=30)
    engine = models.FloatField()
