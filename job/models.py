from random import choice

from django.db import models


# Create your models here.
class Job(models.Model):
    JOB_TYPE = (("Full Time", "Full Time"), ("Part Time", "Part Time"))

    title = models.CharField(max_length=100)
    job_type = models.CharField(choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
