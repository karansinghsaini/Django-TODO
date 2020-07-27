from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title