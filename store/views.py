from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Autores, Generos, Libros, Carrito, CarritoItem, Contacto
from . import views
from .forms import ContactoForm

def index(request):
    return render(request, 'index.html')

def autores(request):
    autores = Autores.objects.all()
    return render(request, 'autores.html', {'autores': autores})

def generos(request):
    generos = Generos.objects.all()
    return render(request, 'generos.html', {'generos': generos})

def libros(request):
    libros = Libros.objects.all()
    return render(request, 'libros.html', {'libros': libros})

def libro_detalle(request, libro_id):
    libro = get_object_or_404(Libros, id=libro_id)
    return render(request, 'libro_detalle.html', {'libro': libro})

@login_required
def carrito(request):
    # Filtrar por usuario y clave de sesión, o crear un nuevo carrito si no existe
    carrito = Carrito.objects.filter(user=request.user, session_key=request.session.session_key).first()
    return render(request, 'carrito.html', {'carrito': carrito})

@login_required
def add_to_cart(request, libro_id):
    libro = get_object_or_404(Libros, id=libro_id)
    # Obtener o crear un carrito para el usuario y sesión actual
    carrito, created = Carrito.objects.get_or_create(user=request.user, session_key=request.session.session_key)
    # Obtener o crear un ítem en el carrito
    cart_item, created = CarritoItem.objects.get_or_create(libros=libro, carrito=carrito)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    # Filtrar por usuario y clave de sesión, o crear un nuevo carrito si no existe
    carrito = Carrito.objects.filter(user=request.user, session_key=request.session.session_key).first()
    if carrito is None:
        carrito = Carrito(user=request.user, session_key=request.session.session_key)
        carrito.save()
    return render(request, 'carrito.html', {'carrito': carrito})

@login_required
def remove_from_cart(request, item_id):
    carrito_item = get_object_or_404(CarritoItem, id=item_id)
    carrito_item.delete()
    return redirect('view_cart')

def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'contacto_formulario.html', {'form': form})

@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'contacto_detalle.html', {'contacto': contacto})

@login_required
def contacto_editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contacto_editar.html', {'form': form})

@login_required
def contacto_eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.delete()
    return redirect('contacto_lista')

@login_required
def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')
