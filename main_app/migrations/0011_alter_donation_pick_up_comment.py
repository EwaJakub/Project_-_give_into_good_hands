# Generated by Django 4.0.4 on 2022-05-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_donation_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='pick_up_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
