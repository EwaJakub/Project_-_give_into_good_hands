# Generated by Django 4.0.4 on 2022-05-05 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_donation2'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='address',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='donations_categories', to='main_app.category'),
        ),
        migrations.AddField(
            model_name='donation',
            name='city',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations_institutions', to='main_app.institution'),
        ),
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='pick_up_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations_institutions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donation',
            name='zip_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
