from django.db import models

class Type(models.Model):
    title = models.CharField(max_length=250)
        
    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
        
class Color(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
        
class Product(models.Model):
    type = models.ManyToManyField(Type, related_name='products')
    image = models.ImageField(upload_to='product/static/img')
    title = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    size = models.ManyToManyField(Size, related_name='products')
    color = models.ManyToManyField(Color, related_name='products')
    number = models.IntegerField()
    
    def __str__(self):
        return f'{self.type} / {self.title}'