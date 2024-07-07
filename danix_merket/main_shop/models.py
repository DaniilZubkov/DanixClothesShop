from django.utils import timezone
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    products = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    size = models.CharField(max_length=50)
    vozvrat = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# qBzVcpZ4-Q мой пароль
