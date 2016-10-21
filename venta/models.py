from django.db import models
from cliente.models import Cliente
from producto.models import Producto


# Create your models here.

class Venta (models.Model):
	cliente=models.ForeignKey(Cliente,null=True,blank=True)
	descuento=models.DecimalField(max_digits = 4,decimal_places=2)
	total=models.DecimalField(max_digits = 6, decimal_places = 2)
	igv=models.DecimalField(max_digits = 6, decimal_places = 2)
	fecha  = models.DateTimeField(auto_now_add=True)
	finalizada=models.BooleanField()
	detalle=models.ForeignKey('DetalleProducto',null=True,blank=True)
	def finalizar(self):
		'''termina la venta y imprime la boleta '''
		...
	def añadirProducto(self,cantidad,producto):
		''' agrega producto a la boleta '''
		...
	def eliminarProducto(self,producto):
		''' eliminar producto  agregada a boleta  por equivocacion '''
		...
	def modificarProducto(self,cantidad,producto):
		''' modifica producto agragada a boleta por quivocacion '''
		...		 	
	def eliminar(self):
		''' elimina una venta finalizada  '''
		...
	def cancelar(self):
		''' cancela una boleta antes de finalizar la venta '''
		...	 	


class DetalleProducto (models.Model):
	producto=models.ForeignKey(Producto,null=True,blank=True)
	cantidad=models.IntegerField()
	precio=models.DecimalField(max_digits = 6, decimal_places = 2)
	
	