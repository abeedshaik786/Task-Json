from django.db import models

# Create your models here.
class Activity_times(models.Model):
    Login_time = models.DateTimeField()
    Logout_time = models.DateTimeField()

class Employee(models.Model):
    Name = models.CharField(max_length=100,blank=True)
    Country = models.CharField(max_length=100,blank=True)
    activity_period = models.ManyToManyField(Activity_times,blank=True)


    def __str__(self):
        return (self.Name)
class Employee_role(models.Model):
    pass
