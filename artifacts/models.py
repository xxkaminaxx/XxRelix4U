from django.db import models
import datetime
# Create your models here.


class Artifact(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField(max_length=105)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    date_posted = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.name
