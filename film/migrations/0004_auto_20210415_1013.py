# Generated by Django 3.1 on 2021-04-15 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20210415_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_profile',
            name='film_image',
            field=models.ImageField(default='default.jpg', upload_to='film_profile'),
        ),
    ]
