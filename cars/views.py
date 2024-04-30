from rest_framework.views import APIView
from cars.models import Car
from cars.serializers import CarSerializer, CarListSerializer

class CarListCreate(APIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarRetrieveUpdateDestroy(APIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarListSerializer
        return CarSerializer
