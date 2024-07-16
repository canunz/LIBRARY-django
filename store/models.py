from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField  # Asegúrate de tener instalado django-ckeditor
from .utils import encrypt_message, decrypt_message

# MODELO AUTOR
class Autores(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='autores/', null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

# MODELO GÉNERO
class Generos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return self.name

# MODELO LIBRO
class Libros(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='libros/')
    stock = models.PositiveIntegerField(default=1)
    autores = models.ForeignKey(Autores, on_delete=models.CASCADE, related_name='libros')
    generos = models.ForeignKey(Generos, on_delete=models.CASCADE, related_name='libros')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.title

# MODELO CONTACTO
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()  # Campo para el mensaje original
    mensaje_cifrado = models.TextField()  # Campo para almacenar el mensaje cifrado
    fecha = models.DateTimeField(auto_now_add=True)  # Añade el campo de fecha

    def save(self, *args, **kwargs):
        # Cifra el mensaje antes de guardarlo
        self.mensaje_cifrado = encrypt_message(self.mensaje)
        super().save(*args, **kwargs)

    def get_mensaje(self):
        # Descifra el mensaje al recuperarlo
        return decrypt_message(self.mensaje_cifrado)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Carrito for {self.user}'

# MODELO ITEM DEL CARRITO
class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    libros = models.ForeignKey(Libros, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item del Carrito'
        verbose_name_plural = 'Items del Carrito'

    def __str__(self):
        return f"{self.libros.title} (x{self.quantity})"
