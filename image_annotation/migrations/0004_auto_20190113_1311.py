# Generated by Django 2.1.4 on 2019-01-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_annotation', '0003_auto_20190113_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labeledimage',
            name='image',
            field=models.ImageField(upload_to='static/uploaded_images/'),
        ),
    ]