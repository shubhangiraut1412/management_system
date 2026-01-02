from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False, blank=False)
    email=models.EmailField(max_length=100, null=False, blank=False, unique=True)
    age=models.IntegerField()
    salary=models.FloatField(blank=True, null=True)
    address=models.CharField(max_length=200,  blank=True, default=None, null=True)
    dob=models.CharField(max_length=100, blank=True, default="01.01.2025", null=True)
    mobile=models.CharField(max_length=14, blank=False, default=None, null=True)
    gender=models.CharField(max_length=100, blank=True, default=None, null=True)
    height=models.CharField(max_length=10, blank=True,default=None, null=True)



    class Meta:
        db_table = 'employee'


    def __str__(self):
        return self.name




