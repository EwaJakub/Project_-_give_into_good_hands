# Generated by Django 4.0.4 on 2022-04-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_donation_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='pick_up_comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
