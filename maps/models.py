from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(verbose_name="Région", max_length=100)
    class_name = models.CharField(verbose_name="Nom de la classe", max_length=10)
    coord = models.CharField(max_length=10000)
    viewbox = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Région'
        verbose_name_plural = "Régions"
        ordering = ['name']

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(verbose_name="Département", max_length=100)
    class_name = models.CharField(verbose_name="Nom de la classe", max_length=10)
    coord = models.CharField(max_length=10000)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='departments')

    class Meta:
        verbose_name = 'Département'
        verbose_name_plural = "Départements"
        ordering = ['name']

    def __str__(self):
        return self.name
