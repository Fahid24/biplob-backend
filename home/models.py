from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/')
    def __str__(self):
        return self.name
