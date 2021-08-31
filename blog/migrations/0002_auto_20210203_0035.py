# Generated by Django 3.1.5 on 2021-02-02 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('citas', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Articulo', 'verbose_name_plural': 'Articulos'},
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('profession', models.CharField(max_length=50, verbose_name='Profesion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.cita', verbose_name='Cita')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['-created_at'],
            },
        ),
    ]
