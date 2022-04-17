from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna'),
)


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE, default=1, null=True)
    categories = models.ManyToManyField(Category, related_name='institutions')

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category, related_name='donations_categories')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='donations_institutions')
    address = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=225)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateTimeField()
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='donations_institutions')

    def __str__(self):
         return self.quantity