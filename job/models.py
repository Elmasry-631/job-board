from random import choice
from uuid import uuid4
from datetime import datetime
from django.db import models
# Create your models here.
def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    unique_name = f"{uuid4().hex}.{ext}"
    today = datetime.today()
    return "jobs/%s" %(instance.title) +"/"+ today.strftime("%Y/%m/%d") + "/" + unique_name
class Job(models.Model):
    JOB_TYPE = (("Full Time", "Full Time"), ("Part Time", "Part Time"), ("Internship", "Internship"), ("Freelance", "Freelance"))
    title = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
