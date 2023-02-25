from django.db import models
from accounts.models import UserProfile


type = (
    ('SP', 'Specials'),
    ('BQ', 'Bouquets'),
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


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()

    def __str__(self):
        return self.title
