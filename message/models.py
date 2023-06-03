from django.db import models
from channel.models import Channel
from contact.models import Contact
from datetime import datetime


class Message(models.Model):

    TYPE = (
        ('text', 'Texto'),
        ('image', 'Imagen'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('document', 'Documento'),
        ('location', 'Ubicación'),
        ('button', 'Boton'),
        ('list', 'Lista'),
    )

    FROM = (
        ('user', 'Usuario'),
        ('contact', 'Contacto')
    )
    
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE, blank=False)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False)
    message = models.TextField(blank=False)  
    timestamp = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length=50, choices=TYPE, default='text')
    origin = models.CharField(max_length=50, choices=FROM)

    def __str__(self):
        return self.contact_id.name
    

class Chat(models.Model):
    isGroupChat = models.BooleanField(default=False)
    channel_id = models.ManyToManyField(Channel, blank=False, related_name='chat_channels')
    contact_id = models.ManyToManyField(Channel, blank=False, related_name='chat_contacts')
    latestMessage = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    