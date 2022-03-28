from django.contrib import admin
from .models import Clientes, Enderecos, Produtos, Alugueis

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
admin.site.register(Clientes, ClientesAdmin)

class EnderecosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Enderecos, EnderecosAdmin)

class ProdutosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Produtos, ProdutosAdmin)

class AlugueisAdmin(admin.ModelAdmin):
    pass
admin.site.register(Alugueis, AlugueisAdmin)