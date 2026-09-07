from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=250)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')

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
    category = models.ManyToManyField(Category, blank=True, related_name='products')
    image = models.ImageField(upload_to='product')
    title = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    size = models.ManyToManyField(Size, blank=True, related_name='products')
    color = models.ManyToManyField(Color, related_name='products')
    quantity = models.IntegerField()
    
    slug = models.SlugField(blank=True, null=True, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)
            self.slug = original_slug
            counter = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        category = self.category.first()
        if category:
            return f'{self.title} | {category.title}'
        return f'{self.title} | No Category'