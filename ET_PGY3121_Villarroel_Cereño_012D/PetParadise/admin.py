from django.contrib import admin

from PetParadise.models import Tienda,detalle_boleta,Boleta

# Register your models here.


admin.site.register(Tienda)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)