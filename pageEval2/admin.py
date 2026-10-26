
from django.contrib import admin
from .models import Categoria, Item, Cuenta, Cuenta_personaje, Personaje

admin.site.register([
    Categoria,
    Item,
    Cuenta,
    Cuenta_personaje,
    Personaje
])
