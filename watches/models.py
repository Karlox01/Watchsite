from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    ebay_link = models.URLField(blank=True, null=True)
    item_offers = models.ManyToManyField('Offer', related_name='items', blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    has_box = models.BooleanField(default=False)
    has_papers = models.BooleanField(default=False)
    water_resistance = models.CharField(max_length=100, blank=True, null=True)
    case_size = models.CharField(max_length=20, blank=True, null=True)
    case_material = models.CharField(max_length=50, blank=True, null=True)
    movement = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Offer(models.Model):
    item = models.ForeignKey(Item, related_name='offers', on_delete=models.CASCADE)
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for currency
    is_accepted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='offers', on_delete=models.CASCADE)

    def __str__(self):
        return f'Offer of ${self.offer_amount} on {self.item.name}'
