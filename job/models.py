from random import choice
from uuid import uuid4
from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    unique_name = f"{uuid4().hex}.{ext}"
    return "jobs/"  + datetime.today().strftime("%Y/%m/%d") + "/" + unique_name

class Job(models.Model): 
    JOB_TYPE = (("Full Time", "Full Time"), ("Part Time", "Part Time"), ("Internship", "Internship"), ("Freelance", "Freelance"))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_owner')
    title = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE)
    description = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Job, self).save(*args, **kwargs) 
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    resume = models.FileField(upload_to=upload_to)
    cover_letter = models.TextField(max_length=500, blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name