from django.contrib import admin
from django.db import models
import base64

# Register your models here.
from base64 import b64decode
import urllib.parse
from urllib.parse import unquote
from django.utils.html import mark_safe
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.admin import DateFieldListFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from . import models

class ConcursosAdmin(admin.ModelAdmin):
    list_display = ('titulo_link','descripcion','expte','fecha_pub','fecha_cad','id_rubro','tipo','lugar_apertura','id_area','nom_archivo','id_subrubro','subrubron1','num')
    list_display_links = None
    search_fields = ('titulo','descripcion','id_rubro__nombre','tipo__nombre','expte','lugar_apertura')
    list_per_page = 10
    list_filter = (
        ('fecha_pub', DateFieldListFilter),('fecha_cad', DateFieldListFilter),'id_rubro','tipo',
    )
    editable_objs = []

    def get_actions(self, request):
        actions = super(ConcursosAdmin, self).get_actions(request) 
        del actions['delete_selected']
        return actions
    
    def titulo_link(self, obj):
        if obj in self.editable_objs:
            return format_html("<a href='{id}'>{titulo}</a>", id=obj.pk, titulo=obj.titulo)
        else:
            return format_html("{titulo}", id=obj.pk, titulo=obj.titulo)

    def get_queryset(self,request):
        q= super().get_queryset(self)
        self.editable_objs = q.filter(fecha_cad__gt=timezone.now())
        return q.filter(is_delete=False)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_area':
            kwargs['queryset'] = models.Areas.objects.filter(listar=1).order_by('nom_area')
        return super(ConcursosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
    
class ConcuAdmin(admin.ModelAdmin):
    list_display = ('titulo_link','descripcion','expte','fecha_pub','fecha_cad','id_rubro','tipo','lugar_apertura','id_area','nom_archivo','id_subrubro','subrubron1','num')
    list_display_links = None
    search_fields = ('titulo','descripcion','id_rubro__nombre','tipo__nombre','expte','lugar_apertura')
    list_per_page = 10
    list_filter = (
        ('fecha_pub', DateFieldListFilter),('fecha_cad', DateFieldListFilter),'id_rubro','tipo',
    )
    editable_objs = []

    def get_actions(self, request):
        actions = super(ConcuAdmin, self).get_actions(request) 
        del actions['delete_selected']
        return actions

    def titulo_link(self, obj):
        if obj in self.editable_objs:
            return format_html("<a href='{id}'>{titulo}</a>", id=obj.pk, titulo=obj.titulo)
        else:
            return format_html("{titulo}", id=obj.pk, titulo=obj.titulo)

    def get_queryset(self,request):
        q= super().get_queryset(self)
        self.editable_objs = q.filter(fecha_cad__gt=timezone.now())
        return q.filter(is_delete=False).filter(visible=True)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'id_area':
            kwargs['queryset'] = models.Areas.objects.filter(listar=1).order_by('nom_area')
        return super(ConcuAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class AutoridadesCopiaAdmin(admin.ModelAdmin):
    list_display = ('apellido','nombre')
    search_fields = ('apellido','nombre')
    list_per_page = 10

class AreasAdmin(admin.ModelAdmin):
    list_display = ('nom_area','direccion','id_aut')
    search_fields = ('nom_area','direccion')
    list_per_page = 10
    def get_queryset(self,request):
        q= super().get_queryset(self)
        return q.filter(listar=1)

class SubrubrosAdmin(admin.ModelAdmin):
    list_display = ('nombre','rubro')
    search_fields = ('nombre','rubro_id__nombre')
    list_per_page = 10

class Subrubron1Admin(admin.ModelAdmin):
    list_display = ('subrubron1','subrubro')
    search_fields = ('subrubron1','subrubro_id__nombre')
    list_per_page = 10


   

    #def decode_titulo(self, obj):
    	#if len(obj.titulo) % 4 != 0: #check if multiple of 4
    	#while len(obj.titulo) % 4 != 0:
    	#	obj.titulo = obj.titulo + "="
    	#	return urllib.parse.unquote(base64.b64decode(obj.titulo).decode('utf-8'))
         #else:

     #return urllib.parse.unquote(base64.b64decode(obj.titulo).decode('utf-8'))
  
    #def save_model(self, request, obj, form, change):
     #   obj.titulo = base64.standard_b64encode(obj.titulo.encode('utf-8'))
     #   obj.save()

 
        



# Register your models here.
admin.site.register(models.Concursos,ConcursosAdmin)
admin.site.register(models.Concu,ConcuAdmin)
admin.site.register(models.Areas,AreasAdmin)
admin.site.register(models.AutoridadesCopia,AutoridadesCopiaAdmin)
admin.site.register(models.Rubro)
admin.site.register(models.Subrubro,SubrubrosAdmin)
admin.site.register(models.Subrubron1,Subrubron1Admin)


