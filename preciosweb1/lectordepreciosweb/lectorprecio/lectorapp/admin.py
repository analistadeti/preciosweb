from django.contrib import admin

# Register your models here.

from .models import PromotionImage,ConsultaProducto
from django.db.models import Sum

@admin.register(PromotionImage)
class PromotionImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image',)

class ConsultaProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo_de_barra', 'contador', 'total_consultas')

    def total_consultas(self, obj):
        return ConsultaProducto.objects.aggregate(Sum('contador'))['contador__sum']

    total_consultas.short_description = 'Total de Consultas'

admin.site.register(ConsultaProducto, ConsultaProductoAdmin)
