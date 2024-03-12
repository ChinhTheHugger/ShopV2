from rest_framework import serializers
from car.models.brand import Brand
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    
    icon_img = serializers.SerializerMethodField('get_img_url')
    
    class Meta:
        model = Brand
        fields = ('id','name','website','desintext','image','icon_img')
    
    def get_img_url(self, obj):
        return obj.image.url