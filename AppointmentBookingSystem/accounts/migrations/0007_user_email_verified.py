# Generated by Django 3.2.9 on 2021-12-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]