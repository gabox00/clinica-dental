from django.contrib import admin
from .models import Category, Article, Employee

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')
    list_display = ('name','created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at','user')
    search_fields = ('title', 'content', 'user__username','categories__name')
    list_display = ('title','user', 'public','created_at')
    list_filter = ('public','user__username','categories__name')

    #Son metodos predeterminados para una determinada funcion.
    #Lo usamos para añadir automaticamente el user_id en un articulo con el usuario en sesion
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name','last_name','created_at', 'update_at','user')
    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id = request.user.id
            obj.first_name = request.user.first_name
            obj.last_name = request.user.last_name
        else:
            obj.first_name = request.user.first_name
            obj.last_name = request.user.last_name
        obj.save()

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Employee, EmployeeAdmin)