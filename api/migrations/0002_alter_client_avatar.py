# Generated by Django 3.2.4 on 2022-01-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='avatar',
            field=models.ImageField(upload_to='static/images/', verbose_name='Аватарка'),
        ),
    ]
