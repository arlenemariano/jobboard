from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    title = models.CharField(max_length=40)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=40)
    email = models.EmailField(blank=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{ self.title } - { self.url }"