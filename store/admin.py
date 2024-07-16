from django.contrib import admin
from .models import Autores, Generos, Libros, Carrito, CarritoItem, Contacto
from .forms import ContactoForm

@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Libros)
class LibrosAdmin(admin.ModelAdmin):
    list_display = ('title', 'autores', 'generos', 'precio', 'stock', 'created_at', 'updated_at')
    search_fields = ('title', 'autores__name', 'generos__name')
    list_filter = ('autores', 'generos')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'created_at', 'updated_at')
    search_fields = ('user__username', 'session_key')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CarritoItem)
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'libros', 'quantity', 'created_at', 'updated_at')
    search_fields = ('libros__title',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    form = ContactoForm
    list_display = ('nombre', 'email', 'fecha')
    search_fields = ('nombre', 'email')
    readonly_fields = ('fecha',)
