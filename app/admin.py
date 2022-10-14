from django.contrib import admin

from .models import Bancos, Clientes, Deuda, Pagos

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Bancos)
admin.site.register(Deuda)
admin.site.register(Pagos)
