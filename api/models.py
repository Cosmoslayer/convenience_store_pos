from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Category(models.Model):    
    name = models.CharField(max_length=100)
    image = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name
