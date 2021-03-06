# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 15:16
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('des_area', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nom_area', models.CharField(blank=True, max_length=80, null=True)),
                ('alias', models.CharField(max_length=27)),
                ('nivel', models.IntegerField(blank=True, editable=False, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=35, null=True)),
                ('email', models.CharField(blank=True, editable=False, max_length=60, null=True)),
                ('id_area_sup', models.SmallIntegerField(blank=True, editable=False, null=True)),
                ('centrex', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('listar', models.CharField(default=1, editable=False, max_length=1)),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'db_table': 'areas',
                'ordering': ['id_area'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Autoridades',
            fields=[
                ('id_aut', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(max_length=70)),
                ('apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('prof', models.CharField(blank=True, max_length=10, null=True)),
                ('curriculum', models.CharField(max_length=60)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('domicilio', models.CharField(blank=True, max_length=45, null=True)),
                ('id_foto', models.IntegerField()),
                ('orden', models.IntegerField()),
            ],
            options={
                'db_table': 'autoridades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AutoridadesCopia',
            fields=[
                ('id_aut', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.CharField(blank=True, max_length=70, null=True)),
                ('apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('prof', models.CharField(blank=True, max_length=10, null=True)),
                ('curriculum', models.CharField(max_length=60)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('domicilio', models.CharField(blank=True, max_length=45, null=True)),
                ('id_foto', models.IntegerField(blank=True, editable=False, null=True)),
                ('orden', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Autoridad',
                'verbose_name_plural': 'Autoridades',
                'db_table': 'autoridades_copia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Concu',
            fields=[
                ('id_concurso', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', ckeditor.fields.RichTextField()),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('nom_archivo', models.FileField(upload_to='', verbose_name='Archivo')),
                ('fecha_pub', models.DateField(verbose_name='Fecha de Publicacion')),
                ('fecha_cad', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('num', models.IntegerField(verbose_name='Numero')),
                ('anio', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Año')),
                ('expte', models.CharField(max_length=15, verbose_name='Expediente')),
                ('lugar_apertura', ckeditor.fields.RichTextField()),
                ('hora_apertura', models.TimeField()),
                ('visible', models.BooleanField(default=True, editable=False)),
                ('is_delete', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name': 'Concu',
                'verbose_name_plural': 'Concu',
                'db_table': 'concursos',
                'ordering': ['-fecha_pub'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Concursos',
            fields=[
                ('id_concurso', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', ckeditor.fields.RichTextField()),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('nom_archivo', models.FileField(upload_to='', verbose_name='Archivo')),
                ('fecha_pub', models.DateField(verbose_name='Fecha de Publicacion')),
                ('fecha_cad', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('num', models.IntegerField(verbose_name='Numero')),
                ('anio', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Año')),
                ('expte', models.CharField(max_length=15, verbose_name='Expediente')),
                ('lugar_apertura', ckeditor.fields.RichTextField()),
                ('hora_apertura', models.TimeField()),
                ('visible', models.BooleanField(default=False, editable=False)),
                ('is_delete', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'verbose_name': 'Concurso',
                'verbose_name_plural': 'Concursos',
                'db_table': 'concursos',
                'ordering': ['-fecha_pub'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('cons_id', models.AutoField(primary_key=True, serialize=False)),
                ('cons_apeynom', models.CharField(max_length=200)),
                ('cons_mail', models.CharField(max_length=30)),
                ('cons_asunto', models.CharField(max_length=200)),
                ('cons_area', models.IntegerField()),
                ('cons_fecha', models.DateField()),
                ('cons_hora', models.DateField()),
                ('cons_msg', models.TextField()),
            ],
            options={
                'db_table': 'consultas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id_respuesta', models.AutoField(primary_key=True, serialize=False)),
                ('id_consulta', models.IntegerField()),
                ('mensaje', models.TextField()),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'respuestas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rubros',
            fields=[
                ('id_rubro', models.AutoField(primary_key=True, serialize=False)),
                ('rubro', models.CharField(max_length=60)),
                ('nivel', models.SmallIntegerField()),
                ('id_sup', models.IntegerField()),
            ],
            options={
                'db_table': 'rubros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('usuario', models.TextField()),
                ('apeynom', models.CharField(max_length=200)),
                ('pass_field', models.TextField(db_column='pass')),
                ('nivel_acceso', models.SmallIntegerField()),
                ('tipo_usuario', models.CharField(max_length=100)),
                ('fechaalta', models.DateField()),
                ('horaalta', models.TimeField()),
                ('fechamodi', models.DateField()),
                ('horamodi', models.TimeField()),
                ('fechabaja', models.DateField()),
                ('horabaja', models.TimeField()),
                ('estado', models.IntegerField()),
                ('area', models.IntegerField()),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Rubro',
                'verbose_name_plural': 'Rubros',
            },
        ),
        migrations.CreateModel(
            name='Subrubro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('rubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concurso.Rubro')),
            ],
            options={
                'verbose_name': 'Subrubro',
                'verbose_name_plural': 'Subrubros',
            },
        ),
        migrations.CreateModel(
            name='Subrubron1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subrubron1', models.CharField(max_length=255)),
                ('subrubro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concurso.Subrubro')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
    ]
