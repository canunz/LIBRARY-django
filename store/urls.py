from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.autores, name='autores'),
    path('generos/', views.generos, name='generos'),
    path('libros/', views.libros, name='libros'),
    path('libro/<int:libro_id>/', views.libro_detalle, name='libro_detalle'),
    path('carrito/', views.view_cart, name='carrito'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('contacto/<int:pk>/editar/', views.contacto_editar, name='contacto_editar'),
    path('contacto/<int:pk>/eliminar/', views.contacto_eliminar, name='contacto_eliminar'),
    path('contacto/', views.contacto_lista, name='contacto_lista'),
    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),
    path('vista_protegida/', views.vista_protegida, name='vista_protegida'),
]

    # path('registro/', views.registro, name='registro'),  # Comentada para futuras referencias

