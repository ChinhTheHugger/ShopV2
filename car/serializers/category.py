from rest_framework import serializers
from car.models.category import Category
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    
    icon_img = serializers.SerializerMethodField('get_img_url')
    
    class Meta:
        model = Category
        fields = ('id','name','image','icon_img')
        
    def get_img_url(self, obj):
        return obj.image.url