# Generated by Django 3.2 on 2022-02-17 21:11

import adoptions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat_details',
            name='cat_photo',
            field=models.ImageField(default='static/adoptions/cat_static.jpg', upload_to=adoptions.models.rename_upload_photo),
        ),
    ]
