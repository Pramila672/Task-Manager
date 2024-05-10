from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    status_choice = [
        ('NS' , 'Not Started'),
        ('IP',  'In Progress'),
        ('CD', 'Completed'),
    ]
    title = models.CharField(max_length=100)
    desc =models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length = 2, choices = status_choice,default ='NS')
    user = models.ForeignKey(User, on_delete = models.CASCADE )

    def __str__(self):
        return self.title