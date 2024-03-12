from rest_framework import serializers
from car.models.manager import Manager
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'