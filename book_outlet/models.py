from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    ratting = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(11)]
        
    )
    author = models.CharField(null=True,max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}({self.ratting})"
