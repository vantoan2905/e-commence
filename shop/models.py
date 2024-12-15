

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

# Mô hình Product
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(default=None, null=True, blank=True)
    price = models.FloatField()
    articleNumber = models.CharField(max_length=255, null=True, blank=True)
    articleType = models.CharField(max_length=255, default='Unspecified')
    productDisplayName = models.CharField(max_length=255, null=True, blank=True)
    masterCategory = models.CharField(max_length=255, null=True, blank=True)
    subCategory = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    baseColour = models.CharField(max_length=255, null=True, blank=True)
    fashionType = models.CharField(max_length=255, null=True, blank=True)
    season = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    usag = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.productDisplayName or "Unnamed Product"



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings',  default=None)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    rating_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} rated {self.product.productDisplayName or 'Unknown Product'} as {self.rating}"

class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_histories')
    query = models.CharField(max_length=255, default=None)
    search_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} searched for '{self.query}'"

class ViewHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='view_histories', default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='view_histories' , default=None)
    view_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} viewed {self.product.productDisplayName or 'Unknown Product'}"

class ClickHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='click_histories', default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='click_histories', default=None)
    click_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} clicked {self.product.productDisplayName or 'Unknown Product'}"

