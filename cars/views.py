#C - Create
#R - Read / Retrieve
#U - Update
#D - Delete / Destroy

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cars.models import Car
from cars.serializers import CarSerializer
from django.http import Http404

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):

        try:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
        except Car.DoesNotExist:
            # return Response('Not found', status.HTTP_404_NOT_FOUND)
            raise Http404()

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data

        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404()

        serializer = CarSerializer(car, data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']

        try:
            Car.objects.get(pk=pk).delete()
        except Car.DoesNotExist:
            raise Http404()

        return Response(status.HTTP_204_NO_CONTENT)

# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         cars = Car.objects.all()
#         res = [{'brand': car.brand, 'price': car.price, 'year': car.year} for car in cars]
#         return Response(res)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         print(data)
#         car = Car.objects.create(**data)
#         return Response(car)
#
# class CarRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         try:
#             car = Car.objects.get(pk=pk)
#             car_res = {'pk': car.pk, 'brand': car.brand, 'price': car.price, 'year': car.year}
#         except Car.DoesNotExist:
#             return Response('Car not found')
#         return Response(car_res)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         try:
#             car = Car.objects.get(pk=pk)
#             for key, value in data.items():
#                 setattr(car, key, value)
#                 car.save()
#         except Car.DoesNotExist:
#             return Response('Car not found')
#         return Response('Car updated')