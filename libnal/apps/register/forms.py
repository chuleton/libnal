from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField(required=True)
	lastname = forms.CharField(required=True)
	
	class Meta:
		model = User
		fields = ('username','name','lastname','email', 'password1', 'password2')

	def save(self, commit = True):
		user = super(UserCreationForm. self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.lastname = self.cleaned_data['lastname']

		if commit:
			user.save()
		
		return user
