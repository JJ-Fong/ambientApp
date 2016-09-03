from django import forms
from .models import UserFieldsTest5

class UserFieldsForm(forms.ModelForm): 
	class Meta:
		model = UserFieldsTest5
		widgets = {
			"password": forms.PasswordInput()
		}
		fields = [ 
			"username",
			"password",
			"email"
		]