from django.db import models
from multiselectfield import MultiSelectField
from django.forms import ModelForm
from smart_selects.db_fields import ChainedForeignKey
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Center(models.Model):
    head = models.CharField(max_length=50)
    center_name = models.CharField(max_length=20)
    center_address = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.center_name)

class User(models.Model):
    username = models.ForeignKey(Center,on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    initial = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    enroll_date = models.DateTimeField()

    def __str__(self):
        return self.initial

class Attendance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_id = models.DateField(default=timezone.now)

