from django.db import models

# Create your models here.
class Mecanicos(models.Model):
    cedula = models.IntegerField(max_length=10)
    nombres = models.CharField(blank=False, max_length=200)
    apellidos = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=10)
    email = models.EmailField()
    estado = models.IntegerField(default=1) #1 si esta activo y 2 si esta eliminado
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "mecanicos"
        verbose_name = "mecanico"
        verbose_name_plural = "mecanicos"

    def __str__(self):
        return self.apellidos + ' ' + self.nombres

class Cliente(models.Model):
    cedula = models.CharField(max_length=200)
    nombre = models.CharField(blank=False, max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=10)
    email = models.EmailField()
    estado = models.IntegerField(default=1)  # 1 si esta activo y 2 si esta eliminado
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Cliente"
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.apellido + ' ' + self.nombre

class Bodega(models.Model):
    codigo = models.CharField(max_length=200)
    repuesto = models.CharField(blank=False, max_length=200)
    valorunidad = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad= models.IntegerField(max_length=7)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Cliente"
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.codigo + ' ' + self.repuesto

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    cedula = models.IntegerField(max_length=10)


