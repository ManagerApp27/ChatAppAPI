from django.db import models
from user.models import Channel
from contact.models import Contact
from django.utils import timezone


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
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, blank=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False)
    message = models.TextField(blank=False)  
    timestamp = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50, choices=TYPE, default='text')
    origin = models.CharField(max_length=50, choices=FROM)

    def __str__(self):
        return self.contact.name