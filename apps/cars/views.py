from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import car_filter
from apps.cars.models import Car
from apps.cars.serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    # queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
