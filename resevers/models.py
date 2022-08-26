from django.db import models

# Create your models here.
class SignUp(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(blank=True)
    contact_no = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20)

class CourierService(models.Model):
    service_choices = (('EXPRESS', 'Express'), ('REGULAR', 'Regular'), ('INTERNATIONAL', 'International'))
    receiver_name = models.CharField(max_length=25)
    contact_number = models.IntegerField(max_length=10)
    area = models.CharField(max_length=30)
    pickup_address = models.TextField(max_length=40)
    delivery_address = models.TextField(max_length=40)
    package_dimension = models.CharField(max_length=25)
    weight = models.CharField(max_length=10)
    service = models.CharField(max_length=13, choices=service_choices, default='EXPRESS')

