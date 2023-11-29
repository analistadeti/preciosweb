from django.db import models

# Create your models here.
class PromotionImage(models.Model):
    image = models.ImageField(upload_to='promotions/')
    alt_text = models.CharField(max_length=200)

    def __str__(self):
        return self.alt_text


class ConsultaProducto(models.Model):
    codigo_de_barra = models.CharField(max_length=100, unique=True)
    contador = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.codigo_de_barra
