from django.urls import path 
from . import views

# el archivo de configuraciones
from django.conf import settings  
# config para mstrar l img
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('mysql/<int:id>', views.query_mysql, name='mysql'),
    path('funcion_query/<int:id>', views.mysql_function, name='funcion_query'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)