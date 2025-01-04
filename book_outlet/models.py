from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    ratting = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(11)]
        
    )
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}({self.ratting})"
