# Generated by Django 3.2.9 on 2021-12-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_appointment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]