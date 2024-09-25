from rest_framework import serializers

from store.models import Dish


class DishSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=512)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_available = serializers.BooleanField()

    def create(self, validated_data):
        return Dish.objects.create(**validated_data)
