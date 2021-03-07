from django.db import models

# Create your models here.
class product(models.Model):
    name =  models.CharField(max_length = 20)
    price = models.IntegerField()
    img = models.ImageField(upload_to = 'pics')

class cart(models.Model):
    prd_id = models.ForeignKey(product,on_delete = models.CASCADE)
    user_id = models.IntegerField()
    #name =  models.CharField(max_length = 20)
    #price = models.IntegerField()
    #img = models.ImageField(upload_to = 'pics')