from django.db import models
import hashlib

class Cliente (models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    email =  models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)
    dni =models.CharField(max_length=8)
    
    def crear(user,password):
        s = cliente()
        s.username = user
        s.password = hashlib.sha256(str(password).encode()).hexdigest()
        s.save()
        return s

    def verificar(user , password):
        try:
            ver =  cliente.objects.get(username=user)   
        except cliente.DoesNotExist:

            return False

        c=hashlib.sha256(str(password).encode()).hexdigest()
        if ver.password==c:            
            return True
        else:
            return False    

             