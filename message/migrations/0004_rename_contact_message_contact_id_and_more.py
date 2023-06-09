# Generated by Django 4.2.1 on 2023-06-02 20:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
        ('message', '0003_alter_message_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='contact',
            new_name='contact_id',
        ),
        migrations.RemoveField(
            model_name='message',
            name='channel',
        ),
        migrations.AddField(
            model_name='message',
            name='channel_id',
            field=models.ForeignKey(default=56415415, on_delete=django.db.models.deletion.CASCADE, to='channel.channel'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isGroupChat', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('channel_id', models.ManyToManyField(related_name='chat_channels', to='channel.channel')),
                ('contact_id', models.ManyToManyField(related_name='chat_contacts', to='channel.channel')),
                ('latestMessage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='message.message')),
            ],
        ),
    ]
