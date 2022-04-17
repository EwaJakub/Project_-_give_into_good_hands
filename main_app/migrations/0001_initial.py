# Generated by Django 4.0.4 on 2022-04-16 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], default=1, null=True)),
                ('categories', models.ManyToManyField(related_name='institutions', to='main_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=225)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=225)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateTimeField()),
                ('categories', models.ManyToManyField(related_name='donations_categories', to='main_app.category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations_institutions', to='main_app.institution')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations_institutions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
