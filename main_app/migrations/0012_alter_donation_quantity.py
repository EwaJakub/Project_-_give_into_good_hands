# Generated by Django 4.0.4 on 2022-05-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_donation_pick_up_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]