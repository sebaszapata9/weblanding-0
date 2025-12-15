from django.urls import path
from . import views

app_name = "core"

#path nos permite tener multiples urls dentro de una lista

urlpatterns = [
	path('',views.home, name="home"),
    path('thanks/', views.thanks, name="thanks"),
	]

# views hace referencia al renderizado html
# home hace referencia a la función creada en archivo views.py
	
"""

que la ruta tenga nomenclatura '' significa que es la ruta principal
ejm: mercadolibre.com.pe/

Si en vez de '' fuera /productos, entonces la dirección a la que haría
referencia sería mercadolibre.com.pe/productos

"""