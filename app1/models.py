from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    concern=models.TextField()
    checks=models.BooleanField()

    def __str__(self):
        return self.name+"--"+self.email