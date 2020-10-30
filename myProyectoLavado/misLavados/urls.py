from django.contrib import admin
from django.urls import path, include
from .views import index, galeria, compra, insumos, login, mision,productos,registro,resenias,ubicación, cerrar,lista_insumos,eliminar_insumo,misionyvision,buscar,modificar
urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('compra/',compra,name='COMP'),
    path('insumos/',insumos,name='INSU'),
    path('login/',login,name='LOGI'),
    path('mision/',misionyvision,name='MISI'),
    path('productos/',productos,name='PROD'),
    path('registro/',registro,name='REGI'),
    path('resenias/',resenias,name='RESE'),
    path('ubicación/',ubicación,name='UBIC'),
    path('logout_sesion/',cerrar,name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LIST'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIM'),
    path('buscar/<id>/',buscar,name='BUSC'),
    path('modificar/',modificar,name='MODI')
]
