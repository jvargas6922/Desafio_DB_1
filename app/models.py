from django.db import models

# Create your models here.
class Conductor(models.Model):
    id_conductor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=9, null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField(null=False)

    class Meta:
        managed = False
        db_table = 'conductor'

    def __str__(self):
        return self.rut

class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6, null=False, unique=True)
    marca = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    anio = models.DateField(null=False)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, db_column='id_conductor')

    class Meta:
        managed = False
        db_table = 'vehiculo'

    def __str__(self):
        return self.patente

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=50, null=False)
    dpto = models.CharField(max_length=10, null=False)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, db_column='id_conductor')

    class Meta:
        managed = False
        db_table = 'direccion'

    def __str__(self):
        return self.calle


