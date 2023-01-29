from django.db import models


type = (
    ('SP', 'Special'),
    ('BQ', 'Bouquet'),
    ('IP', 'Indoor Plants'),
)


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    type = models.CharField(max_length=2, null=True, choices=type)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
