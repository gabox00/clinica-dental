from django.contrib import admin
from .models import Cita, TipoCita

# Register your models here.
class CategoryCita(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at','user')

    #Son metodos predeterminados para una determinada funcion.
    #Lo usamos para añadir automaticamente el user_id en un articulo con el usuario en sesion
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

class CategoryTipoCita(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')

admin.site.register(Cita, CategoryCita)
admin.site.register(TipoCita, CategoryTipoCita)