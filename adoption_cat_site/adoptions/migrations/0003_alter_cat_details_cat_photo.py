# Generated by Django 3.2 on 2022-01-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_cat_details_cat_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_details',
            name='cat_photo',
            field=models.ImageField(default='static/adoptions/cat_static.jpg', upload_to='adoptions/'),
        ),
    ]
