# Generated by Django 3.1.5 on 2021-02-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0007_auto_20210203_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipocita',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Nombre'),
        ),
    ]
