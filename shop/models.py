from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    date = models.DateTimeField()
    price = models.FloatField()
    stock = models.IntegerField()
    sold = models.IntegerField()
    rating = models.FloatField()
    image = models.ImageField(upload_to="shop/static/shop/img/")

    def __str__(self):
        return self.name
