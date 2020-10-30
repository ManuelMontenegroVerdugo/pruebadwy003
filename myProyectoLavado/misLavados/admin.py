from django.contrib import admin
from .models import SliderIndex
from .models import SliderGaleria
from .models import Insumos
from .models import MisionyVision

# Register your models here.

class SliderIndexAdmin(admin.ModelAdmin):
    list_display = ['ident','image']
    search_fields =['ident']
    list_per_page = 10


class SliderGaleriaAdmin(admin.ModelAdmin):
    list_display = ['ident1','image1']
    search_fields =['ident1']
    list_per_page = 10


class InsumosAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','stock']
    search_fields =['nombre', 'precio']
    list_per_page = 10

class MisionyVisionAdmin(admin.ModelAdmin):
    list_display = ['ident','mision','vision']
    search_fields =['mision']
    list_per_page = 10

admin.site.register(SliderIndex,SliderIndexAdmin)
admin.site.register(SliderGaleria,SliderGaleriaAdmin)
admin.site.register(Insumos,InsumosAdmin)
admin.site.register(MisionyVision,MisionyVisionAdmin)


