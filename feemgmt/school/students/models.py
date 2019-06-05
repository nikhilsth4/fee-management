from django.db import models
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User
# Create your models here.
class StudentModel(models.Model):
    Std_id=models.PositiveIntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=200)
    Class=models.PositiveIntegerField()
    Mobile_no=models.BigIntegerField()
    M='M'
    F='F'
    GENDER_CHOICES = (
    (M, 'Male'),
    (F, 'Female'),
    )
    Gender=models.CharField(
    max_length=1,
    choices=GENDER_CHOICES,
    default=M)
    Academic_year=models.PositiveIntegerField()
    Branch=models.CharField(max_length=30)
    def __str__(self):
        return str(self.Std_id)
    # def get_absolute_url(self):
    #     return reverse('student-detail',kwargs={'pk':self.pk})

    # installing crispy forms in update
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update'))

class FeesModel(models.Model):
	Name=models.CharField(max_length=100)
	Std_id=models.ForeignKey(StudentModel,on_delete=models.CASCADE)
	Receipt_no=models.IntegerField()
	Total_fees=models.IntegerField()
	def __str__(self):
		return self.Name
	# def get_absolute_url(self):
	# 	return reverse('fees-detail',kwargs={'pk':self.pk})


class ResourceProfile(models.Model):
    usernames=models.CharField(max_length=255,default=None)
    password=models.CharField(max_length=255,default=None)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    citizen_no=models.IntegerField(default=None)
    job=models.CharField(max_length=255,null=True,default=None)
    points=models.IntegerField(max_length=255,default=None)
    random=models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.usernames

class Generalprofile(models.Model):
    username=models.CharField(max_length=255,default=None)
    password=models.CharField(max_length=255,default=None)

