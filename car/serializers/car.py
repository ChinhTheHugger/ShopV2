from rest_framework import serializers
from car.models.car import Car
class CarSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    
    front_img = serializers.SerializerMethodField('get_front_url')
    back_img = serializers.SerializerMethodField('get_back_url')
    interior_img = serializers.SerializerMethodField('get_interior_url')
    
    class Meta:
        model = Car
        fields = ('id','name','price','model','brand','category','year','desintext','front','back','interior','instock','front_img','back_img','interior_img')
        
    def get_front_url(self, obj):
        return obj.front.url
    def get_back_url(self, obj):
        return obj.back.url
    def get_interior_url(self, obj):
        return obj.interior.url