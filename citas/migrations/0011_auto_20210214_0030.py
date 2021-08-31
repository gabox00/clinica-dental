# Generated by Django 3.1.5 on 2021-02-13 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0010_auto_20210213_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cita',
            name='accepted',
        ),
        migrations.AddField(
            model_name='cita',
            name='coments',
            field=models.TextField(default='', verbose_name='Comentario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cita',
            name='status',
            field=models.SmallIntegerField(default=2, verbose_name='Estado de la cita'),
        ),
    ]