# Generated by Django 3.1.5 on 2021-02-03 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_employee_cita'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el')),
            ],
            options={
                'verbose_name': 'Tipo de cita',
                'verbose_name_plural': 'Tipos de citas',
            },
        ),
        migrations.AddField(
            model_name='cita',
            name='employee',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.employee', verbose_name='Empleado'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='cita',
            name='typeof',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='citas.tipocita', verbose_name='Tipo de cita'),
        ),
    ]
