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

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE, default=1, null=True)
    categories = models.ManyToManyField(Category, related_name='institutions')

    class Meta:
        verbose_name = 'institution'
        verbose_name_plural = 'institutions'

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category, related_name='donations_categories', blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='donations_institutions', blank=True, null=True)
    address = models.CharField(max_length=225, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=225, blank=True, null=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    pick_up_date = models.DateField(blank=True, null=True)
    pick_up_time = models.TimeField(blank=True, null=True)
    pick_up_comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='donations_institutions')
    is_taken = models.BooleanField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'donation'
        verbose_name_plural = 'donations'

    def __str__(self):
         return self.city

