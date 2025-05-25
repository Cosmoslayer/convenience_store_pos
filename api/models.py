from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Category(models.Model):    
    name = models.CharField(max_length=100)
    image = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='items',blank=True,
                                 null=True)
    description = models.CharField(max_length=100)
    buying_price = models.DecimalField(max_digits=11, decimal_places=2)
    selling_price = models.DecimalField(max_digits=11, decimal_places=2)
    stock = models.IntegerField()
    image = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self) -> str:
        return self.description

