from django.db import models

# Create your models here.
class Employee_table(models.Model):
    EMP_NAME=models.CharField(max_length=300)
    EMP_DES=models.CharField(max_length=300)
    EMP_Place=models.CharField(max_length=300)

