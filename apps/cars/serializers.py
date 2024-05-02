from rest_framework import serializers
from apps.cars.views import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car

        # fields = '__all__'
        fields = ('id', 'brand', 'price', 'year', 'seats', 'body_type', 'engine', 'created_at', 'updated_at')


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car

        fields = ('id', 'brand', 'year')
