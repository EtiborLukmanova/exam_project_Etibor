from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Sweets(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    company = models.CharField(max_length=30)
    image_sweet = models.ImageField(default=False, upload_to='media/sweets_images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sweets_table'


class CustomUserComment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    sweet = models.ForeignKey(Sweets, on_delete=models.CASCADE)
    comment = models.TextField()
    star_given = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.create_at}'

    class Meta:
        db_table = 'comment'

