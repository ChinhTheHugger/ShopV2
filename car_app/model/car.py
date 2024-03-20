from django.db import models

class Car(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    model= models.CharField(max_length=50,null=True)
    brand= models.IntegerField(default=0)
    category= models.IntegerField(default=0)
    year= models.IntegerField(default=0)
    desintext= models.CharField(max_length=250, default='', blank=True, null= True)
    front= models.ImageField(upload_to='uploads/fronts/')
    back= models.ImageField(upload_to='uploads/backs/')
    interior= models.ImageField(upload_to='uploads/interiors/')
    instock= models.IntegerField(default=0)

    @staticmethod
    def get_cars_by_id(ids):
        return Car.objects.filter (id__in=ids)
    @staticmethod
    def get_all_cars():
        return Car.objects.all()

    @staticmethod
    def get_all_cars_by_categoryid(category_id):
        if category_id:
            return Car.objects.filter (category=category_id)
        else:
            return Car.get_all_cars()
    
    class Meta:
        db_table = 'car'