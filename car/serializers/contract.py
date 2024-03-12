from rest_framework import serializers
from car.models.contract import Contract
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'