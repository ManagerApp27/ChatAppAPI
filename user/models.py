from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #campos atributos de django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email
    

class Channel(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivar'),
    )

    user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, blank=False)
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
    

# class WhatsAppTokens(models.Model):
#     STATUS = (
#         ('True', 'Activo'),
#         ('False', 'Desactivar'),
#     )

#     channel = models.OneToOneField(Channel, on_delete=models.CASCADE, blank=False)
#     name = models.CharField(max_length=50, blank=False)
#     whatsapp_toke = models.CharField(max_length=300, blank=False)
#     channel_toke = models.CharField(max_length=100, blank=False)
#     status = models.CharField(max_length=10, choices=STATUS, default=True)
#     created = models.DateField(auto_now_add=True)
#     updated = models.DateField(auto_now=True)


#     def __str__(self):
#         return self.name
    
