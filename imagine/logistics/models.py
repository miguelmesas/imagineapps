from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)


class Package(models.Model):
    weight = models.FloatField()
    dimensions = models.CharField(max_length=50)
    delivery_status = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class VehicleType(models.Model):
    type = models.CharField(max_length=50, null=True)


class Carrier(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    packages = models.ManyToManyField(Package)
