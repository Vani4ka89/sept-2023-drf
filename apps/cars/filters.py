from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.cars.models import Car


def car_filter(query: QueryDict) -> QuerySet:
    qs = Car.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)
            case _:
                raise ValidationError(f"{k} is not valid")
    return qs
