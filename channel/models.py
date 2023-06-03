from django.db import models
from user.models import UserAccount

class Channel(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivar'),
    )

    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS, default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Canales'

    def __str__(self):
        return self.name
    

class WhatsAppTokens(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivar'),
    )

    channel_id = models.OneToOneField(Channel, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50, blank=False)
    secret_key = models.CharField(max_length=300, blank=False)
    token = models.CharField(max_length=300, blank=False)
    url_id = models.CharField(max_length=300, blank=False)
    version = models.CharField(max_length=300, blank=False)
    status = models.CharField(max_length=10, choices=STATUS, default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    def __str__(self):
        return self.name
