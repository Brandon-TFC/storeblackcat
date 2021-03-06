from django.db import models
from users.models import User
# Create your models here.

# Se crea la DB 
class DireccionEnvio(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=300)
    line2 = models.CharField(max_length=300, blank=True)
    city =  models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    reference = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=6, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # Sobreescribe con postal_code
    def __str__(self):
        return self.postal_code
    
    def update_default(self, default=False):
        self.default = default
        self.save()
    
    def has_orden(self):
        return self.orden_set.count() >= 1

    @property
    def direccion(self): # Funcion que devuelve atributos 'line1, 'city' y 'state'
        return '{}, {}, {},'.format(self.line1, self.city, self.state,)