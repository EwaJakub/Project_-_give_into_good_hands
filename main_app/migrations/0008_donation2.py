# Generated by Django 4.0.4 on 2022-05-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_donation_address_remove_donation_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
