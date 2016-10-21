from django.db import models

# Create your models here.

class Producto (models.Model):
	
	nombre= models.CharField(max_length=45)
	descripcion=models.TextField()
	precio=models.DecimalField(max_digits = 6, decimal_places = 2)
	tipo=models.CharField(max_length=45)
	
		
