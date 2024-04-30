from rest_framework.response import Response
from rest_framework.views import APIView
from cars.models import Car

class CarTestView(APIView):
    def get(self, *args, **kwargs):
        return Response("Hello from get")

    def post(self, *args, **kwargs):
        data = self.request.data
        params_dict = self.request.query_params.dict()
        print(params_dict)
        print(data)
        return Response("Hello from post")

    def put(self, *args, **kwargs):
        return Response("Hello from put")

    def patch(self, *args, **kwargs):
        return Response("Hello from patch")

    def delete(self, *args, **kwargs):
        return Response("Hello from delete")

class CarDetailView(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response("Hello from")


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = Car.objects.all()
        res = [{'id': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year} for car in cars]
        return Response(res)

    def post(self, *args, **kwargs):
        data = self.request.data
        Car.objects.create(**data)
        return Response("Car created")
