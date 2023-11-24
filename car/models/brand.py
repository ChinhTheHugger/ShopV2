from django.db import models

class Brand(models.Model):
    name= models.CharField(max_length=50)
    website= models.CharField(max_length=50)
    desintext= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/brands/')

    @staticmethod
    def get_all_categories():
        return Brand.objects.all()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'brand'