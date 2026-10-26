
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Personaje(models.Model):
    raza = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    nivel = models.PositiveIntegerField()
    ban = models.BooleanField(default=False)
    creado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.raza} - Nivel {self.nivel}"


class Cuenta(models.Model):
    usuario = models.CharField(max_length=80, unique=True)
    correo = models.EmailField(max_length=120)

    def __str__(self):
        return self.usuario


class Cuenta_personaje(models.Model):
    cuenta = models.ForeignKey(
        Cuenta,
        on_delete=models.CASCADE,
        related_name="cuentas_personajes"
    )
    personaje = models.ForeignKey(
        Personaje,
        on_delete=models.CASCADE,
        related_name="cuentas_personajes"
    )

    def __str__(self):
        return f"{self.cuenta} - {self.personaje}"


class Item(models.Model):
    personaje = models.ForeignKey(
        Personaje,
        on_delete=models.CASCADE,
        related_name="items"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="items"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.PositiveIntegerField()
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return self.nombre
