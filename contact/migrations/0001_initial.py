# Generated by Django 4.2 on 2023-04-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('neighborhood', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('True', 'Activo'), ('False', 'Desactivar')], default=True, max_length=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]