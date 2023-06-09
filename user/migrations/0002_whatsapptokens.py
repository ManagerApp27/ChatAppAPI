# Generated by Django 4.2.1 on 2023-05-28 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsAppTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('whatsapp_toke', models.CharField(max_length=300)),
                ('channel_toke', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('True', 'Activo'), ('False', 'Desactivar')], default=True, max_length=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('channel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.channel')),
            ],
        ),
    ]
