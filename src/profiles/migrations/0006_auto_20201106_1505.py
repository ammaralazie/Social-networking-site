# Generated by Django 3.1.2 on 2020-11-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20201106_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media_root/avatar.jpg', upload_to='avatar/'),
        ),
    ]