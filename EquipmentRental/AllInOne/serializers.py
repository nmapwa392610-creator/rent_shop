from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Equipment,Customer, Rental

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['full_name', 'phone', 'email']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'category', 'description', 'price_per_day', 'serial_number', 'is_available', 'created_at']

class RentalSerializer(serializers.ModelSerializer):
    customer_details = CustomerSerializer(source='customer', read_only=True)

    class Meta:
        model = Rental
        fields = ['id', 'name', 'customer', 'customer_details', 'start_date', 'end_date', 'total_price', 'status_active']
