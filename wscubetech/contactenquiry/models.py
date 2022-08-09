from django.db import models


class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField()


# Create your models here.
