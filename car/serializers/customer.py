from rest_framework import serializers
from car.models.customer import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'