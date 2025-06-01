from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from datetime import datetime
# Create your models here.


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.product_name}.{ext}'
    unique_name = uuid4().hex + ext
    today = datetime.now()
    return f'products/{unique_name}'



class AddProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to=upload_to)

    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True,)

    def __str__(self):
        return self.product_name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)
