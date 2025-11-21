from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=100 )
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
