# Generated by Django 3.2 on 2022-08-17 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerce', '0005_ciudad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('f_creacion', models.DateTimeField(auto_now_add=True)),
                ('f_modificacion', models.DateTimeField(auto_now=True)),
                ('user_updated', models.IntegerField(blank=True, null=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('celular', models.IntegerField()),
                ('email', models.EmailField(max_length=350)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.ciudad')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]