from django.shortcuts import render
import pyodbc
from .models import PromotionImage,ConsultaProducto

def buscar_producto(request):
    descripcion = ""
    precio_formateado = ""

    # Obtener todas las imágenes de promociones
    images = PromotionImage.objects.all()

    if request.method == 'POST':
        id_producto = request.POST.get('id_producto', '')

        if id_producto:
            try:
                server = '192.168.32.102'
                database = 'zeusprueba'
                username = 'roxanne'
                password = 'Cr@2_no680*1996'
                conn = pyodbc.connect(
                    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

                sql_query = "SELECT DESCRIPCION, VVENTA FROM PS_PRODUCTO WHERE CODIGODEBARRA = ?"
                cursor = conn.cursor()
                cursor.execute(sql_query, id_producto)
                producto = cursor.fetchone()

                if producto:
                    descripcion = producto[0]
                    precio_formateado = "{:,.0f}".format(producto[1])
                consulta, created = ConsultaProducto.objects.get_or_create(codigo_de_barra=id_producto)
                consulta.contador += 1
                consulta.save()

                conn.close()
            except pyodbc.Error as e:
                mensaje = f"Error de base de datos:\n{str(e)}"

    return render(request, 'search_result.html',
                  {'descripcion': descripcion, 'precio_formateado': precio_formateado, 'images': images})

# Otras vistas y funciones aquí...

def consulta_producto_view(request):
    productos = ConsultaProducto.objects.all()
    total_contador = sum(producto.contador for producto in productos)

    context = {
        'productos': productos,
        'total_contador': total_contador,
    }
    return render(request, 'consulta_producto.html', context)

