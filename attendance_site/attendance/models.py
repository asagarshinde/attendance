from django.db import models
from multiselectfield import MultiSelectField
from django.forms import ModelForm

# Create your models here.


class center(models.Model):
    head = models.CharField(max_length=50)
    center_name = models.CharField(max_length=20)
    center_address = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.center_name)

class user(models.Model):
    username = models.ForeignKey(center,on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    initial = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    enroll_date = models.DateTimeField()

    def __str__(self):
        return self.initial

class attendance(models.Model):
    userid = models.ForeignKey(user,on_delete=models.CASCADE)
    date_id = models.DateField()

class CenterForm(ModelForm):
    class Meta:
        model = center
        fields = ['head']