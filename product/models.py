from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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
    image = models.ImageField(upload_to='product')
    title = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    size = models.ManyToManyField(Size, related_name='products')
    color = models.ManyToManyField(Color, related_name='products')
    number = models.IntegerField()
    slug = models.SlugField(default="", null=False, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug: 
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.type} / {self.title}'