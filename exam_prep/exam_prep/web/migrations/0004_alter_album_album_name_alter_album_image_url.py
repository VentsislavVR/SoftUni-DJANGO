# Generated by Django 4.2.5 on 2023-09-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_album_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Album Name'),
        ),
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]