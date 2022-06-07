from django.db import models

class Product(models.Model):
    name = models.CharField(
        max_length=222,
        blank=True,
        null=True,
        db_index=True,
        default='No name'
    )
    description = models.TextField(
        blank=True
    )
    image = models.ImageField(
        upload_to='images',
        blank=True
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    is_published = models.BooleanField(
        default=True,
    )
    in_stock = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Employer(models.Model):
    photo = models.ImageField(
        upload_to='image/employers/',
        blank=True
    )
    name = models.CharField(
        max_length=222
    )
    position = models.CharField(
        max_length=222
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    is_published = models.BooleanField(
        default=True,
    )
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']







