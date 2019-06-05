from django import forms
from .models import FeesModel,ResourceProfile,Generalprofile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FeesForm(forms.ModelForm):
	class Meta:
		model=FeesModel
		fields ='__all__'


class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=('username','email','password1','password2')


class SignupR(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=ResourceProfile
		fields=('usernames','password')

class SignupG(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Generalprofile
		fields='__all__'
