from rest_framework import serializers
from cars.views import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    seats = serializers.IntegerField()
    body_type = serializers.CharField(max_length=30)
    engine = serializers.FloatField()

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
            return instance


class CarListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
