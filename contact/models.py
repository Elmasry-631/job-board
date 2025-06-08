from django.db import models

# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Info'
   
