# Generated by Django 4.0.4 on 2022-05-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_donation_address_donation_categories_donation_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]