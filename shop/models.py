from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.slug}'

class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category.title} - {self.title} - {self.slug}'

class Product(models.Model):
    QUANTITY_TYPE_CHOICES = (
        ('kg', 'Kilogram'),
        ('lb','Pound')
    )

    owner = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    thumbnail = models.URLField()
    quantity_type = models.CharField(max_length=5, choices=QUANTITY_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, related_name="products", on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.owner.username}-{self.title}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.subcategory.title} - {self.title} - {self.price}'


class Invoice(models.Model):
    user = models.ForeignKey(User, related_name="invoices", on_delete=models.CASCADE)
    summary = models.TextField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    card_token = models.TextField()
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']