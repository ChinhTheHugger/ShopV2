from django.db import models

class Manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_manager_by_email(email):
        try:
            return Manager.objects.get(email= email)
        except:
            return False
    
    @staticmethod
    def get_manager_by_id(customer_id):
        return Manager.objects.filter(id=customer_id)


    def isExists(self):
        if Manager.objects.filter(email = self.email):
            return True

        return False
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    
    class Meta:
        db_table = 'manager'