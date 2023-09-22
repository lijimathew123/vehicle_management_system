from django.db import models

# Create your models here.
class User(models.Model):
    ROLE =(
        ('super_admin','super_admin'),
        ('admin','admin'),
        ('user','user')
    )
    name=models.CharField(max_length=150)
    email = models.EmailField(max_length=200, default='null')
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=150)
    role=models.CharField(max_length=20, choices=ROLE)
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Two', 'Two Wheeler'),
        ('Three', 'Three Wheeler'),
        ('Four', 'Four Wheeler'),
    )

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()



    def __str__(self):
        return self.vehicle_number
    

