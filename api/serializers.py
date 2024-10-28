from rest_framework import serializers

from store.models import Dish, Restaurant, Menu, Order, OrderItem, Payment, Customer, Courier


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        exclude = ('created_at', 'updated_at')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ('created_at', 'updated_at')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        exclude = ('created_at', 'updated_at')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ('created_at', )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'
