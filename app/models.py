from django.db import models
from django.forms import CharField, IntegerField


class Bancos(models.Model):
    nombreB = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreB


class Clientes(models.Model):
    nombreC = models.CharField(max_length=50)
    Cedula = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreC


class Deuda(models.Model):
    banco = models.ForeignKey(Bancos, null=False, blank=True, on_delete=models.CASCADE, default=0)
    cliente = models.ForeignKey(Clientes, null=False, blank=True, on_delete=models.CASCADE, default=0)
    total_deuda = models.IntegerField()
    total_cuotas = models.IntegerField()


class Pagos(models.Model):
    deuda = models.ForeignKey(Deuda, related_name="pagos", null=False, blank=True, on_delete=models.CASCADE, default=0)
    valor_pago = models.IntegerField()
    cuotas = models.IntegerField()
