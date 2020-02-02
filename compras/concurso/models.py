from __future__ import unicode_literals
import base64
from base64 import b64decode,b64encode
from django.core.validators import MaxLengthValidator
from django.db import models
from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey 
from django.core.validators import MaxValueValidator

   
class Tipo(models.Model):
    nombre= models.CharField(max_length=255)
    def __str__(self):
        return str(self.nombre)

class Estado(models.Model):
    nombre= models.CharField(max_length=255)
    def __str__(self):
        return str(self.nombre)

class Rubro(models.Model):
    nombre = models.CharField(max_length=255)
     
    def __str__(self):
        return str(self.nombre)
    class Meta:
        
        verbose_name = 'Rubro'
        verbose_name_plural = 'Rubros' 

       

class Subrubro(models.Model):
    rubro = models.ForeignKey(Rubro)
    nombre = models.CharField(max_length=255,verbose_name="Subrubro")
    

    def __str__(self):
        return str(self.nombre)
    class Meta:
        
        verbose_name = 'Subrubro'
        verbose_name_plural = 'Subrubros'   

class Subrubron1(models.Model):
    subrubro = models.ForeignKey(Subrubro)
    subrubron1 = models.CharField(max_length=255,verbose_name="Item")
   
    def __str__(self):
        return str(self.subrubron1)
    class Meta:
        
        verbose_name = 'Item'
        verbose_name_plural = 'Items' 

class AutoridadesCopia(models.Model):
    id_aut = models.AutoField(primary_key=True)
    area = models.CharField(max_length=70,blank=True, null=True,editable=False)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    prof = models.CharField(max_length=10, blank=True, null=True,verbose_name="Profesión")
    curriculum = models.CharField(max_length=60,editable=False)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    domicilio = models.CharField(max_length=45, blank=True, null=True)
    id_foto = models.IntegerField(editable=False,blank=True, null=True)
    orden = models.IntegerField()

    def __str__(self):
            return '{}  {}'.format(self.apellido ,self.nombre )

    class Meta:
        managed = False
        db_table = 'autoridades_copia'
        verbose_name = 'Autoridad'
        verbose_name_plural = 'Autoridades'
        
      


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    des_area = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'area'
        


class Areas(models.Model):
    id_area = models.AutoField(primary_key=True)
    nom_area = models.CharField(max_length=80, blank=True, null=True)
    alias = models.CharField(max_length=27,null=True,blank=True)
    id_aut  = models.ForeignKey(AutoridadesCopia,verbose_name="Autoridad")
    nivel = models.IntegerField(blank=True, null=True,editable=False)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=35, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True,editable=False)
    id_area_sup = models.SmallIntegerField(blank=True, null=True,editable=False)
    centrex = models.CharField(max_length=10, blank=True, null=True,editable=False)
    listar = models.CharField(max_length=1,default=1,editable=False)
    def __str__(self):
        return str(self.nom_area)
    class Meta:
        managed = False
        ordering = ["nom_area"]
        db_table = 'areas'
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'


class Autoridades(models.Model):
    id_aut = models.AutoField(primary_key=True)
    area = models.CharField(max_length=70)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    prof = models.CharField(max_length=10, blank=True, null=True)
    curriculum = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    domicilio = models.CharField(max_length=45, blank=True, null=True)
    id_foto = models.IntegerField()
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'autoridades'


from smart_selects.db_fields import ChainedForeignKey 

class Concursos(models.Model):
    id_concurso = models.AutoField(primary_key=True)
    titulo = RichTextField()
    descripcion = RichTextField()
    nom_archivo =models.FileField(verbose_name="Archivo")
    fecha_pub = models.DateField(verbose_name="Fecha de Publicacion")
    fecha_cad = models.DateField(verbose_name="Fecha de Vencimiento")
    tipo = models.ForeignKey(Tipo)
    estado = models.ForeignKey(Estado)
    num = models.IntegerField(verbose_name="Numero")
    anio = models.IntegerField( validators=[MaxValueValidator(9999)],verbose_name="Año")
    expte = models.CharField(max_length=15,verbose_name="Expediente")
    
    id_area = models.ForeignKey(Areas,verbose_name="Area", blank=True, null=True)
    id_rubro = models.ForeignKey(Rubro,verbose_name="Rubro") 
    id_subrubro = ChainedForeignKey(
        Subrubro, # the model where you're populating your countries from
        chained_field="id_rubro", # the field on your own model that this field links to 
        chained_model_field="rubro", # the field on Country that corresponds to newcontinent
        show_all=False, # only shows the countries that correspond to the selected continent in newcontinent
        verbose_name="Subrubro"
    )
    subrubron1=ChainedForeignKey(Subrubron1,chained_field="id_subrubro", chained_model_field="subrubro",verbose_name="Item")
    lugar_apertura = RichTextField()
    hora_apertura = models.TimeField()
    visible = models.BooleanField(default=False,editable=False,db_column='tipo')
    is_delete = models.BooleanField(default=False,editable=False)

    class Meta:
        ordering = ["-fecha_pub"]
        managed = False
        db_table = 'concursos'
        verbose_name = 'Concurso'
        verbose_name_plural = 'Concursos'

    def __str__(self):
         return 'id: {} \n\n Concursos: {} \n\n Descripción {}'.format(self.id_concurso,self.titulo ,self.descripcion )
        

    def delete(self):
        self.is_delete = True
        self.save()

    def delete_hard(self):
        super(Concursos, self).delete()

class Concu(models.Model):
    id_concurso = models.AutoField(primary_key=True)
    titulo = RichTextField()
    descripcion = RichTextField()
    nom_archivo =models.FileField(verbose_name="Archivo")
    fecha_pub = models.DateField(verbose_name="Fecha de Publicacion")
    fecha_cad = models.DateField(verbose_name="Fecha de Vencimiento")
    tipo = models.ForeignKey(Tipo)
    estado = models.ForeignKey(Estado)
    num = models.IntegerField(verbose_name="Numero")
    anio = models.IntegerField( validators=[MaxValueValidator(9999)],verbose_name="Año")
    expte = models.CharField(max_length=15,verbose_name="Expediente")
    
    id_area = models.ForeignKey(Areas,verbose_name="Area", blank=True, null=True)
    id_rubro = models.ForeignKey(Rubro,verbose_name="Rubro") 
    id_subrubro = ChainedForeignKey(
        Subrubro, # the model where you're populating your countries from
        chained_field="id_rubro", # the field on your own model that this field links to 
        chained_model_field="rubro", # the field on Country that corresponds to newcontinent
        show_all=False, # only shows the countries that correspond to the selected continent in newcontinent
        verbose_name="Subrubro"
    )
    subrubron1=ChainedForeignKey(Subrubron1,chained_field="id_subrubro", chained_model_field="subrubro",verbose_name="Item")
    lugar_apertura = RichTextField()
    hora_apertura = models.TimeField()
    visible = models.BooleanField(default=True,editable=False,db_column='tipo')
    is_delete = models.BooleanField(default=False,editable=False)

    class Meta:
        ordering = ["-fecha_pub"]
        managed = False
        db_table = 'concursos'
        verbose_name = 'Concu'
        verbose_name_plural = 'Concu'

    def __str__(self):
        return 'id: {} \n\n Concursos: {} \n\n Descripción {}'.format(self.id_concurso,self.titulo ,self.descripcion )

    def delete(self):
        self.is_delete = True
        self.save()

    def delete_hard(self):
        super(Concursos, self).delete()



class Consultas(models.Model):
    cons_id = models.AutoField(primary_key=True)
    cons_apeynom = models.CharField(max_length=200)
    cons_mail = models.CharField(max_length=30)
    cons_asunto = models.CharField(max_length=200)
    cons_area = models.IntegerField()
    cons_fecha = models.DateField()
    cons_hora = models.DateField()
    cons_msg = models.TextField()

    class Meta:
        managed = False
        db_table = 'consultas'


class Respuestas(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    id_consulta = models.IntegerField()
    mensaje = models.TextField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'respuestas'


class Rubros(models.Model):
    id_rubro = models.AutoField(primary_key=True)
    rubro = models.CharField(max_length=60)
    nivel = models.SmallIntegerField()
    id_sup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rubros'


class Usuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    usuario = models.TextField()
    apeynom = models.CharField(max_length=200)
    pass_field = models.TextField(db_column='pass')  # Field renamed because it was a Python reserved word.
    nivel_acceso = models.SmallIntegerField()
    tipo_usuario = models.CharField(max_length=100)
    fechaalta = models.DateField()
    horaalta = models.TimeField()
    fechamodi = models.DateField()
    horamodi = models.TimeField()
    fechabaja = models.DateField()
    horabaja = models.TimeField()
    estado = models.IntegerField()
    area = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
