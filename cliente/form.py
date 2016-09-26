
from django import forms
from .models import  cliente


class FormularioRegistro(forms.ModelForm):
	class Meta:
		model = cliente
		fields = ['username','password','email','first_name','last_name','dni']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

		