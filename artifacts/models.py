from django.db import models

# Create your models here.


class Artifact(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name