from django.db import models
from user.models import UserAccount


class Contact(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivar'),
    )

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    neighborhood = models.CharField(max_length=50, blank=True)
    status = models.CharField(
    max_length=10, choices=STATUS, default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.name
    
     