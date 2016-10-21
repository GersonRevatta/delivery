
from django import forms
from .models import  Cliente


class FormularioRegistro(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ['username','password','email','first_name','last_name','dni']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

		