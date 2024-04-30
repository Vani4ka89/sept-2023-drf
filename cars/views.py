from rest_framework import generics
from cars.models import Car
from cars.serializers import CarSerializer, CarListSerializer

class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarListSerializer
        return CarSerializer
