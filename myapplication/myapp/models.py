from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    Manager = 1
    Employee = 2
    
    ROLE_CHOICES = (
        (Manager,'Manager'),
        (Employee,'Employee')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank = True, null = True)

class Manager(models.Model):
    ref = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="man")

    class Meta:
        db_table = "manager"

class UserDetails(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    dob=models.DateField()

    def __str__(self):
        return self.name
    class Meta:
        db_table="user_details"