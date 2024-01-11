from django.contrib import admin
from .models.conta import Conta
from .models.cliente import Cliente

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Conta)