# Generated by Django 4.0.4 on 2022-05-05 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_donation_is_taken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='address',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='city',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='is_taken',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='pick_up_comment',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='pick_up_date',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='zip_code',
        ),
    ]
