# Generated by Django 4.2.4 on 2023-08-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(default='asd', max_length=15),
            preserve_default=False,
        ),
    ]
