"""
URL configuration for webkumateq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

]

"""si en el path definido para la app core ponemos '' 
quiere decir que es la ruta principal"""

"""si en vez de '' ponemos /productos, entonces la 
dirección a la que haría que sea web.com.pe/productos"""

""" 
include nos permite incluir urls de otra app, tenemos que usarla siempre excepto
para admin, que eso ya tiene ruta preconfigurada admin.site.urls

la función path siempre solicitará 2 argumentos, ruta url y la vista



"""