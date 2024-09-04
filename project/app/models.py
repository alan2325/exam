from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.TextField()
    email=models.EmailField()
    phone=models.IntegerField()
    alt=models.IntegerField()
    image=models.FileField()

    def __str__(self):
        return self.name