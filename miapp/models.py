from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Review(models.Model):
    juego = models.CharField(max_length=100)
    resena = models.TextField()
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.juego} - {self.calificacion}"
