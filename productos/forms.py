from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(forms.ModelForm):
	#email=forms.id_email()

	class Meta:
		model = Usuario
		fields=['id_email','Password']