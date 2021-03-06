from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(verbose_name="Région",
                            max_length=100)
    class_name = models.CharField(verbose_name="Nom de la classe",
                                  max_length=10)
    coord = models.CharField(max_length=10000)
    viewbox = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Région'
        verbose_name_plural = "Régions"
        ordering = ['name']

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(verbose_name="Département",
                            max_length=100)
    class_name = models.CharField(verbose_name="Nom de la classe",
                                  max_length=10)
    coord = models.CharField(max_length=10000)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='departments')

    class Meta:
        verbose_name = 'Département'
        verbose_name_plural = "Départements"
        ordering = ['name']

    def __str__(self):
        return self.name


class Favorite(models.Model):
    title = models.CharField(verbose_name="Titre",
                             max_length=1000)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='articles')

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = "Favoris"
        ordering = ['title']

    def __str__(self):
        return self.title
