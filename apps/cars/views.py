from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cars.filters import car_filter
from apps.cars.models import Car
from apps.cars.serializers import CarSerializer

# Variant 5___________________


class CarListCreateView(ListCreateAPIView):
    # queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# Variant 4_____________Mixins


# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


# from django.db.models import Q
# from rest_framework.views import APIView
# from cars.filters import car_filter
# from django.http import Http404

# from rest_framework import status
# from rest_framework.response import Response

# Variant 3____________Generics


# class CarListCreateView(GenericAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarListSerializer
#
#     def get(self, *args, **kwargs):
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#
# def post(self, *args, **kwargs):
#     data = self.request.data
#     serializer = self.get_serializer(data=data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         serializer = self.get_serializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = self.get_serializer(car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#         car = self.get_object()
#         serializer = self.get_serializer(car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         self.get_object().delete()
#         return Response(status.HTTP_204_NO_CONTENT)

# Variant 2_____________________


# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#
#         try:
#             qs = car_filter(self.request.query_params.dict())
#             serializer = CarListSerializer(qs, many=True)
#         except Car.DoesNotExist:
#             raise Http404()
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#         car = get_object_or_404(Car, pk=pk)
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         car = get_object_or_404(Car, pk=pk)
#         serializer = CarSerializer(car, data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#         car = get_object_or_404(Car, pk=pk)
#         serializer = CarSerializer(car, data, partial=True)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#         get_object_or_404(Car, pk=pk).delete()
#         return Response(status.HTTP_204_NO_CONTENT)


# Variant 1_________________

# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#
#         try:
#             # cars = Car.objects.filter(brand='Mercedes', year=2008)
#             # cars = Car.objects.filter(brand__in=['Mercedes', 'Ford'], year=2008)
#             # cars = Car.objects.filter(brand__contains='e')
#             # cars = Car.objects.filter(year__range=(2008, 2020))
#             # cars = Car.objects.filter(year__range=(2008, 2020)).order_by('-year')
#             # cars = Car.objects.order_by('-year', '-id')
#             # qs = Car.objects.filter(brand='Ford')
#             # qs = Car.objects.all().exclude(brand='Ford')
#             # qs = qs[1:2].only('id', 'brand')
#             # print(qs.query)
#             # print(qs)
#             # qs = Car.objects.filter(Q(brand='Ford') | Q(year=2008) & Q(pk=2))
#             # count = Car.objects.all().count()
#             # cars = Car.objects.all()
#             # serializer = CarListSerializer(qs, many=True)
#             qs = car_filter(self.request.query_params.dict())
#             serializer = CarListSerializer(qs, many=True)
#         except Car.DoesNotExist:
#             # return Response('Not found', status.HTTP_404_NOT_FOUND)
#             raise Http404()
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             car = Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404()
#
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#
#         try:
#             car = Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404()
#
#         serializer = CarSerializer(car, data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs['pk']
#         data = self.request.data
#
#         try:
#             car = Car.objects.get(pk=pk)
#         except Car.DoesNotExist:
#             raise Http404()
#
#         serializer = CarSerializer(car, data, partial=True)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs['pk']
#
#         try:
#             Car.objects.get(pk=pk).delete()
#         except Car.DoesNotExist:
#             raise Http404()
#
#         return Response(status.HTTP_204_NO_CONTENT)
